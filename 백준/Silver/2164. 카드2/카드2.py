import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
deq = deque(i+1 for i in range(N))

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    deq.popleft()
    deq.append(deq.popleft())