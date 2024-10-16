import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(x + y)+'\n')