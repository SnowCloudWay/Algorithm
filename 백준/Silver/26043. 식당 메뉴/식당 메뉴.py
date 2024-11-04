import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
a, b, c = [], [], []

n = int(input())
for _ in range(n):
    command = list(map(int, input().split()))

    if command[0] == 1:
        dq.append([command[1], command[2]])
    else:
        student = dq.popleft()
        if command[1] == student[1]:
            a.append(student[0])
        else:
            b.append(student[0])

while dq:
    waitStudent = dq.popleft()
    c.append(waitStudent[0])

if len(a) != 0:
    a.sort()
    sys.stdout.write(' '.join(map(str, a)) + '\n')
else:
    sys.stdout.write("None\n")
if len(b) != 0:
    b.sort()
    sys.stdout.write(' '.join(map(str, b)) + '\n')
else:
    sys.stdout.write("None\n")
if len(c) != 0:
    c.sort()
    sys.stdout.write(' '.join(map(str, c)))
else:
    sys.stdout.write("None")