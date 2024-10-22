import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    xn = input().strip()
    dq = deque(xn[1:-1].split(','))
    if n == 0:
        dq = deque()
    error = 0
    R = 0

    for i in range(len(p)):
        if p[i] == 'R':
            R += 1
        elif p[i] == 'D':
            if len(dq) == 0:
                sys.stdout.write('error\n')
                error = 1
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    if error == 1:
        continue
    else:
        if R % 2 == 0:
            sys.stdout.write('['+','.join(dq)+']\n')
        else:
            dq.reverse()
            sys.stdout.write('[' + ','.join(dq) + ']\n')