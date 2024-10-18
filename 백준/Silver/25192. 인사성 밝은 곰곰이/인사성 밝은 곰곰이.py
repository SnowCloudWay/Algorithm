import sys
input = sys.stdin.readline

n = int(input())
s = set()
cnt = 0

for _ in range(n):
    record = input().strip()
    if record == 'ENTER':
        cnt += len(s)
        s = set()
    else:
        s.add(record)
cnt += len(s)

sys.stdout.write(str(cnt))