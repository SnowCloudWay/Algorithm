import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cnt = 0
for _ in range(n):
    seat = [int(i) for i in input().strip()]
    interval_sum = sum(seat[:k])
    if interval_sum == 0:
        cnt += 1
    start, end = 0, k
    while end < m:
        interval_sum -= seat[start]
        interval_sum += seat[end]
        start += 1
        end += 1
        if interval_sum == 0:
            cnt += 1

sys.stdout.write(str(cnt))