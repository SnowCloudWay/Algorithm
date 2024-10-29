import sys
input = sys.stdin.readline

n, game = input().split()
s = set(sys.stdin.read().splitlines())
cnt = 0

if game == 'Y':
    cnt = len(s)
elif game == 'F':
    cnt = len(s) // 2
else:
    cnt = len(s) // 3

sys.stdout.write(str(cnt))