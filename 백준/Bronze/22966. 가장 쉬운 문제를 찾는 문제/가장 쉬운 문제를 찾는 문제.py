import sys
input = sys.stdin.readline

d = dict()
n = int(input())

for _ in range(n):
    a, b = input().strip().split()
    d[int(b)] = a

s_d = sorted(d.items())

print(s_d[0][1])