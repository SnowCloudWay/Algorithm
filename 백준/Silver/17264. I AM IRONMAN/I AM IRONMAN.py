import sys
input = sys.stdin.readline

score = 0
d = {}

n, p = map(int, input().split())
w, l, g = map(int, input().split())

for _ in range(p):
    name, result = input().split()
    d[name] = result

for _ in range(n):
    name = input().strip()
    if name in d:
        if d[name] == 'W':
            score += w
        else:
            score -= l
    else:
        score -= l
    if score < 0:
        score = 0
    elif score >= g:
        sys.stdout.write("I AM NOT IRONMAN!!")
        break
else:
    sys.stdout.write("I AM IRONMAN!!")