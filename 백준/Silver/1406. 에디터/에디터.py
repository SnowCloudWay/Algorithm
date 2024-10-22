import sys
from collections import deque
input = sys.stdin.readline

S = list(input().strip())
dq = deque()
N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == 'L' and S:
        dq.appendleft(S.pop())
    elif command[0] == 'D' and dq:
        S.append(dq.popleft())
    elif command[0] == 'B' and S:
        S.pop()
    elif command[0] == 'P':
        S.append(command[1])

sys.stdout.write(''.join(S) + ''.join(dq))