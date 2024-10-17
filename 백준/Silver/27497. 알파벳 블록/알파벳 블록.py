import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()
stack = []

for _ in range(n):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == '1':
        dq.append(command[1])
        stack.append(command[0])
    elif command[0] == '2':
        dq.appendleft(command[1])
        stack.append(command[0])
    elif command[0] == '3':
        if len(stack) != 0:
            r = stack[-1]
            if r == '1':
                dq.pop()
                stack.pop()
            else:
                dq.popleft()
                stack.pop()

if len(dq) != 0:
    sys.stdout.write(''.join(dq))
else:
    print(0)