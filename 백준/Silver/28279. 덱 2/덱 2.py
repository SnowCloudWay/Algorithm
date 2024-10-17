import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        dq.appendleft(command[1])
    elif command[0] == 2:
        dq.append(command[1])
    elif command[0] == 3:
        if len(dq) != 0:
            print(dq.popleft())
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 4:
        if len(dq) != 0:
            print(dq.pop())
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 5:
        print(len(dq))
    elif command[0] == 6:
        if len(dq) == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif command[0] == 7:
        if len(dq) != 0:
            print(dq[0])
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 8:
        if len(dq) != 0:
            print(dq[-1])
        else:
            sys.stdout.write('-1\n')