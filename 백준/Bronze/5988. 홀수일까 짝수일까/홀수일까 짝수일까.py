import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        sys.stdout.write('even\n')
    else:
        sys.stdout.write('odd\n')