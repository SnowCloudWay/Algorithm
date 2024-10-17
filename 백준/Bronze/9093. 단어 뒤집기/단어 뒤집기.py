import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = list(map(str, sys.stdin.readline().split()))
    for i in s:
        sys.stdout.write(''.join(i[::-1]) + ' ')