import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(list)
couple = []
cnt = 0

n = int(input())
for _ in range(n):
    name, ring = input().split()
    if ring != '-':
        d[ring].append(name)

for key, value in d.items():
    if len(value) == 2:
        cnt += 1
        couple.append(value)

sys.stdout.write(str(cnt)+'\n')
if cnt != 0:
    for i in range(cnt):
        sys.stdout.write(str(couple[i][0]) + " " + str(couple[i][1]) + '\n')