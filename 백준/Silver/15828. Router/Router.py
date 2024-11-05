import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
n = int(input())

while True:
    num = int(input())
    if num == -1: break
    if num != 0:
        if len(dq) < n:
            dq.append(num)
    else:
        dq.popleft()

if dq:
    sys.stdout.write(' '.join(map(str, dq)))
else:
    sys.stdout.write("empty")