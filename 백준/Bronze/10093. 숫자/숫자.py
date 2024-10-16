import sys

a, b = map(int, sys.stdin.readline().split())
l = []

if a < b:
    for i in range(a+1, b):
        l.append(i)
else:
    for i in range(b+1, a):
        l.append(i)

print(len(l))
print(*l)