"""
Codeforces API client with local JSON caching and robust offline fallbacks.
Fetches problem metadata (titles, tags, ratings, URLs) from the official
Codeforces API (https://codeforces.com/api/problemset.problems) and preserves
previously verified data locally.
"""

from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import sys
from typing import Dict, List, Optional, Tuple

import requests

from config import (
    API_TIMEOUT_SECONDS,
    CACHE_FILE,
    CF_API_PROBLEMS_URL,
    CF_CODE_PATTERN,
    METADATA_DIR,
)

logger = logging.getLogger("codeforces_api")


class CodeforcesAPI:
    """Manages Codeforces problem metadata retrieval and local disk caching."""

    def __init__(self, cache_file: Path = CACHE_FILE):
        self.cache_file = cache_file
        self.cache_data: Dict = {"_comment": "Codeforces problem metadata cache", "problems": {}}
        self._api_fetched = False
        self._remote_problems_map: Dict[Tuple[int, str], dict] = {}
        self.load_cache()

    def load_cache(self) -> None:
        """Loads cached problem metadata from disk."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict) and "problems" in data:
                        self.cache_data = data
                    elif isinstance(data, dict):
                        self.cache_data = {"problems": data}
            except Exception as e:
                logger.warning("Failed to parse cache file %s: %s. Re-initializing cache.", self.cache_file, e)
                self.cache_data = {"problems": {}}

    def save_cache(self) -> None:
        """Atomically saves the metadata cache to disk in UTF-8 formatting."""
        try:
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
            self.cache_data["last_updated"] = datetime.now(timezone.utc).isoformat()
            
            temp_file = self.cache_file.with_suffix(".tmp")
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(self.cache_data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            
            temp_file.replace(self.cache_file)
        except Exception as e:
            logger.error("Error saving metadata cache to %s: %s", self.cache_file, e)

    def fetch_api_problemset(self) -> bool:
        """
        Queries https://codeforces.com/api/problemset.problems.
        Returns True if successful, False if network or API error occurs.
        """
        if self._api_fetched:
            return bool(self._remote_problems_map)

        self._api_fetched = True
        try:
            headers = {"User-Agent": "Antigravity-README-Automation/2.0 (GitHubActions; +https://github.com/NguyenVinhHung2705/ICPC_)"}
            response = requests.get(CF_API_PROBLEMS_URL, headers=headers, timeout=API_TIMEOUT_SECONDS)
            if response.status_code != 200:
                logger.warning(
                    "Codeforces API returned HTTP %s: %s",
                    response.status_code,
                    response.reason,
                )
                return False

            data = response.json()
            if data.get("status") != "OK":
                logger.warning("Codeforces API response error: %s", data.get("comment", "Unknown"))
                return False

            problems = data.get("result", {}).get("problems", [])
            for p in problems:
                cid = p.get("contestId")
                idx = p.get("index")
                if cid is not None and idx:
                    self._remote_problems_map[(cid, idx.upper())] = p

            logger.info("Successfully fetched %d problems from Codeforces API.", len(self._remote_problems_map))
            return True

        except requests.exceptions.Timeout:
            logger.warning("Codeforces API timed out after %s seconds. Using local cache.", API_TIMEOUT_SECONDS)
        except requests.exceptions.RequestException as e:
            logger.warning("Codeforces API network error: %s. Using local cache.", e)
        except Exception as e:
            logger.warning("Unexpected error during Codeforces API fetch: %s", e)

        return False

    @staticmethod
    def parse_problem_code(problem_code: str) -> Tuple[Optional[int], Optional[str]]:
        """
        Extracts contestId and index from a problem code string (e.g. '112A' -> (112, 'A')).
        Returns (None, None) if not a standard Codeforces format.
        """
        match = CF_CODE_PATTERN.match(problem_code)
        if match:
            contest_id = int(match.group(1))
            index = match.group(2).upper()
            return contest_id, index
        return None, None

    @staticmethod
    def build_codeforces_url(contest_id: Optional[int], index: Optional[str]) -> Optional[str]:
        """Constructs the canonical Codeforces problem URL."""
        if contest_id is not None and index:
            return f"https://codeforces.com/problemset/problem/{contest_id}/{index}"
        return None

    def resolve_problem(
        self,
        problem_code: str,
        expected_rating: Optional[int] = None,
        readme_fallback_title: Optional[str] = None,
        force_refresh: bool = False,
    ) -> dict:
        """
        Resolves problem metadata:
        1. Checks local cache unless force_refresh is True.
        2. If not cached, fetches from Codeforces API.
        3. Falls back to README existing title or 'Not retrieved' / 'Unknown'.
        """
        cached = self.cache_data.get("problems", {}).get(problem_code)
        if cached and not force_refresh:
            # Check if cached data has a valid name
            if cached.get("name") and cached["name"] not in ("Unknown", "Not retrieved"):
                return cached

        contest_id, index = self.parse_problem_code(problem_code)
        cf_url = self.build_codeforces_url(contest_id, index)

        # Non-Codeforces problem or unparseable ID
        if contest_id is None or index is None:
            name = readme_fallback_title or "Unknown"
            result = {
                "contestId": None,
                "index": None,
                "name": name,
                "rating": expected_rating,
                "tags": [],
                "url": None,
                "is_codeforces": False,
            }
            return result

        # Attempt API lookup
        if not self._api_fetched:
            self.fetch_api_problemset()

        remote_problem = self._remote_problems_map.get((contest_id, index))
        if remote_problem:
            name = remote_problem.get("name")
            rating = remote_problem.get("rating") or expected_rating
            tags = remote_problem.get("tags", [])
            resolved = {
                "contestId": contest_id,
                "index": index,
                "name": name,
                "rating": rating,
                "tags": tags,
                "url": cf_url,
                "is_codeforces": True,
            }
            self.cache_data.setdefault("problems", {})[problem_code] = resolved
            return resolved

        # If not found in API or API failed
        if cached and cached.get("name") and cached["name"] not in ("Unknown", "Not retrieved"):
            return cached

        fallback_name = readme_fallback_title or "Not retrieved"
        fallback_data = {
            "contestId": contest_id,
            "index": index,
            "name": fallback_name,
            "rating": expected_rating,
            "tags": [],
            "url": cf_url,
            "is_codeforces": True,
        }
        self.cache_data.setdefault("problems", {})[problem_code] = fallback_data
        return fallback_data

