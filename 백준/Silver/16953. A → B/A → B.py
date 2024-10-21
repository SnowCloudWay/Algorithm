import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1

while a != b:
    if a > b:
        sys.stdout.write('-1')
        break
    if b % 2 == 0:
        b = b // 2
    elif b % 10 == 1:
        b = b // 10
    else:
        sys.stdout.write('-1')
        break
    cnt += 1
else:
    sys.stdout.write(str(cnt))