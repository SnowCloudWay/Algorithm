import sys
input = sys.stdin.readline

d = {}
n = int(input())
students = list(input().split())

for student in students:
    d[student] = 0

for _ in range(n):
    s = list(input().split())
    for i in s:
        d[i] += 1

s_d = sorted(d.items(), key=lambda item:(-item[1], item[0]))

for k, v in s_d:
    sys.stdout.write(k + ' ' + str(v) + '\n')