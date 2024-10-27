import sys
input = sys.stdin.readline

d = {"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}
bell = False
n = int(input())

for _ in range(n):
    name, num = map(str, input().split())
    d[name] += int(num)

for i in d.values():
    if i == 5:
        bell = True
        break

if bell:
    sys.stdout.write('YES')
else:
    sys.stdout.write('NO')