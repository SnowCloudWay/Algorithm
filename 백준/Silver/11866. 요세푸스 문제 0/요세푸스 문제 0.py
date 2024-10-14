import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
dq = deque(i for i in range(1, n+1))

sys.stdout.write('<')

while n > 1:
    dq.rotate(-(k-1))
    sys.stdout.write(str(dq.popleft()))
    sys.stdout.write(', ')
    n -= 1

sys.stdout.write(str(dq.popleft()) + '>')