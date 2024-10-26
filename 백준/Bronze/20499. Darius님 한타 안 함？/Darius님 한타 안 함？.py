import sys
input = sys.stdin.readline

k, d, a = map(int, input().split('/'))

if k + a < d or d == 0:
    sys.stdout.write('hasu')
else:
    sys.stdout.write('gosu')