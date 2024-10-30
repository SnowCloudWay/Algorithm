import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    nums = [input().strip() for _ in range(n + m)]
    d = defaultdict(int)
    cnt = 0

    for num in nums:
        d[num] += 1

    for v in d.values():
        if v == 2:
            cnt += 1

    sys.stdout.write(str(cnt)+'\n')