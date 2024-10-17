import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()
dqq = deque()

for _ in range(n):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == '1':
        dq.append(command[1])
        dqq.append(command[0])
    elif command[0] == '2':
        dq.appendleft(command[1])
        dqq.append(command[0])
    elif command[0] == '3':
        if len(dqq) != 0:
            r = dqq[-1]
            if r == '1':
                dq.pop()
                dqq.pop()
            else:
                dq.popleft()
                dqq.pop()

if len(dq) != 0:
    sys.stdout.write(''.join(dq))
else:
    print(0)