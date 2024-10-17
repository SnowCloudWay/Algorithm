import sys

t, s = map(int, sys.stdin.readline().split())

if t >= 12 and t <= 16 and s == 0:
    print(320)
else:
    print(280)
