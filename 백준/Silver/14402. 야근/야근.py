import sys
input = sys.stdin.readline

d = {}
cnt = 0

n = int(input())

for _ in range(n):
    name, work = input().split()
    if work == '-':
        if name not in d or d[name] == 0:
            cnt += 1
        else:
            d[name] -= 1
    else:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1

if len(d) == 0:
    sys.stdout.write(str(cnt))
else:
    sys.stdout.write(str(sum(d.values()) + cnt))