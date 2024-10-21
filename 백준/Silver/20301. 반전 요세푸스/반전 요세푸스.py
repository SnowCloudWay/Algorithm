import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split())
dq = deque(i for i in range(1, N+1))
rl = True
cnt = 0

while N >= 1:
    if cnt == M:
        cnt = 0
        if rl is True:
            rl = False
        else:
            rl = True
    if rl is True:
        dq.rotate(-(K - 1))
    else:
        dq.rotate(K)
    sys.stdout.write(str(dq.popleft())+'\n')
    cnt += 1
    N -= 1