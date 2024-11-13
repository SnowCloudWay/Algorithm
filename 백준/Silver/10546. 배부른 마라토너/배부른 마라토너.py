import sys
from collections import defaultdict
input = sys.stdin.readline

dd = defaultdict(int)

n = int(input())
for _ in range(n):
    dd[input().strip()] += 1

for _ in range(n-1):
    name = input().strip()
    dd[name] -= 1
    if dd[name] == 0:
        del dd[name]

sys.stdout.write(''.join(dd.keys()))