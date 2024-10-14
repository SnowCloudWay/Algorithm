import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        if len(dq) != 0:
            sys.stdout.write(str(dq.popleft() + '\n'))
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'size':
        sys.stdout.write(str(len(dq)) + '\n')
    elif command[0] == 'empty':
        if len(dq) != 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write('1\n')
    elif command[0] == 'front':
        if len(dq) != 0:
            sys.stdout.write(dq[0] + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'back':
        if len(dq) != 0:
            sys.stdout.write(dq[-1] + '\n')
        else:
            sys.stdout.write('-1\n')