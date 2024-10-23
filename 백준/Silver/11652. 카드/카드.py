import sys
from collections import defaultdict
input = sys.stdin.readline

dd = defaultdict(int)
N = int(input())
for _ in range(N):
    dd[int(input())] += 1

sorted_dd = sorted(dd.items(), key=lambda item: (-item[1], item[0]))
sys.stdout.write(str(sorted_dd[0][0]))