import sys

n = int(sys.stdin.readline())

stack = list(map(int, sys.stdin.read().splitlines()))

last = stack[-1]
cnt = 1

for s in stack[::-1]:
    if s > last:
        last = s
        cnt += 1

print(cnt)