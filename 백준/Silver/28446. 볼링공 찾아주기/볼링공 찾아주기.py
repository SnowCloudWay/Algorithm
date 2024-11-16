import sys
input = sys.stdin.readline

d = {}

for _ in range(int(input())):
    command = list(map(int, input().split()))
    if command[0] == 1:
        d[command[2]] = command[1]
    else:
        sys.stdout.write(str(d[command[1]]) + '\n')