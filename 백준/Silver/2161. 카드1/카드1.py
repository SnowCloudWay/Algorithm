import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque(i for i in range(1, n+1))

while True:
    if len(dq) == 1:
        break
    sys.stdout.write(str(dq.popleft())+' ')
    dq.append(dq.popleft())

sys.stdout.write(str(dq[0]))