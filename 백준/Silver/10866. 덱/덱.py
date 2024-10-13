import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dq = deque()

for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if len(dq) != 0:
            sys.stdout.write(str(dq.popleft()) + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'pop_back':
        if len(dq) != 0:
            sys.stdout.write(str(dq.pop()) + '\n')
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
            sys.stdout.write(str(dq[0]) + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'back':
        if len(dq) != 0:
            sys.stdout.write(str(dq[-1]) + '\n')
        else:
            sys.stdout.write('-1\n')