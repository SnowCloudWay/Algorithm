import sys
input = sys.stdin.readline

d = {'ChongChong':1}

n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if a in d == False:
        d[a] = 0
    if b in d == False:
        d[b] = 0
    if d.get(a) == 1 or d.get(b) == 1:
        d[a] = 1
        d[b] = 1

cnt = 0
for value in d.values():
    if value == 1:
        cnt += 1

sys.stdout.write(str(cnt))