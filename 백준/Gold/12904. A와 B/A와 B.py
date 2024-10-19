import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

while True:
    if len(t) < len(s):
        sys.stdout.write('0')
        break
    elif s == t:
        sys.stdout.write('1')
        break
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
