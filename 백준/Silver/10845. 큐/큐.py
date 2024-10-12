import sys
from queue import Queue

n = int(sys.stdin.readline().rstrip())
que = Queue()

for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    if command[0] == 'push':
        que.put(command[1])
    elif command[0] == 'pop':
        if que.qsize() != 0:
            sys.stdout.write(que.get() + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'size':
        sys.stdout.write(str(que.qsize()) + '\n')
    elif command[0] == 'empty':
        if que.qsize() == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif command[0] == 'front':
        if que.qsize() != 0:
            sys.stdout.write(que.queue[0] + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'back':
        if que.qsize() != 0:
            sys.stdout.write(que.queue[-1] + '\n')
        else:
            sys.stdout.write('-1\n')