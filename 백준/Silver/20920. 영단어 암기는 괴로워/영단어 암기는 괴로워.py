import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)
n, m = map(int, input().split())

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        d[word] += 1

sorted_d = dict(sorted(d.items(), key=lambda item:(-item[1], -len(item[0]), item[0])))

for word in sorted_d:
    sys.stdout.write(word+'\n')