import sys

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    if command[0] == 'push':
        stack.append(int(command[1]))
    if command[0] == 'pop':
        if len(stack) <= 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(stack.pop()) + '\n')
    elif command[0] == 'size':
        sys.stdout.write(str(len(stack)) + '\n')
    elif command[0] == 'empty':
        if len(stack) <= 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif command[0] == 'top':
        if len(stack) > 0:
            sys.stdout.write(str(stack[-1]) + '\n')
        else:
            sys.stdout.write('-1\n')