import sys
input = sys.stdin.readline

n, game = input().split()
s = set(sys.stdin.read().splitlines())
cnt = 0

match game:
    case 'Y':
        cnt = len(s)
    case 'F':
        cnt = len(s) // 2
    case _:
        cnt = len(s) // 3

sys.stdout.write(str(cnt))