import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = sorted(list(map(int, input().split())))
start, end = 0, n-1
intervalSum = 0
cnt = 0

while start < end:
    intervalSum = w[start] + w[end]
    if intervalSum <= k:
        cnt += 1
        start += 1
        end -= 1
    elif intervalSum > k:
        end -= 1
    else:
        start += 1

sys.stdout.write(str(cnt))