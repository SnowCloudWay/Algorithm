import sys
from collections import deque
input = sys.stdin.readline

do, su = deque(), deque()
do_g, su_g = deque(), deque()
do_gg, su_gg = 0, 0

n, m = map(int, input().split())
for _ in range(n):
    d, s = map(int, input().split())
    do.append(d)
    su.append(s)

for i in range(m):
    if i % 2 == 0:
        do_gg = do.pop()
        do_g.append(do_gg)
    else:
        su_gg = su.pop()
        su_g.append(su_gg)

    if len(do) == 0 or len(su) == 0:
        break

    if do_gg == 5 or su_gg == 5:
        if su_g:
            do.extendleft(su_g)
            su_g.clear()
            su_gg = 0
        if do_g:
            do.extendleft(do_g)
            do_g.clear()
            do_gg = 0

    elif do_g and su_g and do_gg + su_gg == 5:
        su.extendleft(do_g)
        do_g.clear()
        do_gg = 0
        su.extendleft(su_g)
        su_g.clear()
        su_gg = 0

if len(do) > len(su):
    sys.stdout.write('do')
elif len(do) < len(su):
    sys.stdout.write('su')
else:
    sys.stdout.write('dosu')