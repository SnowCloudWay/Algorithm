import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

interval_sum = 0
end = 0
cnt = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += a[end]
        end += 1
    if interval_sum == m:
        cnt += 1
    interval_sum -= a[start]

sys.stdout.write(str(cnt))