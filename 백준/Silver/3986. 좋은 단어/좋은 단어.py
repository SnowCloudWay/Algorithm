import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    stack = []
    s = list(input().strip())
    for i in s:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        cnt += 1

sys.stdout.write(str(cnt))