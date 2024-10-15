import sys

n = int(sys.stdin.readline().rstrip())
s = []

for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        s.append(command[1])
    elif command[0] == 2:
        if len(s) != 0:
            sys.stdout.write(str(s.pop()) + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 3:
        sys.stdout.write(str(len(s)) + '\n')
    elif command[0] == 4:
        if len(s) != 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write('1\n')
    elif command[0] == 5:
        if len(s) != 0:
            sys.stdout.write(str(s[-1]) + '\n')
        else:
            sys.stdout.write('-1\n')