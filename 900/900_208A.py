import sys

s = input()

sys.stdout.write(' '.join(s.replace('WUB', ' ').strip().split()))