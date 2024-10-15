import sys

n, m = map(int, sys.stdin.readline().split())
d = {}
l = []

for _ in range(n+m):
    name = sys.stdin.readline().rstrip()
    if name not in d:
        d[name] = 0
    else:
        d[name] = 1

for k, v in d.items():
    if v == 1:
        l.append(k)

sys.stdout.write(str(len(l))+'\n')
for i in sorted(l):
    sys.stdout.write(i+'\n')