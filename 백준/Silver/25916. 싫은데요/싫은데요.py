import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
intervalSum = 0
end = 0
maxSum = 0

for start in range(n):
    while intervalSum <= m and end < n:
        intervalSum += a[end]
        end += 1
    if intervalSum <= m:
        maxSum = max(maxSum, intervalSum)
    else:
        maxSum = max(maxSum, intervalSum - a[end-1])
    intervalSum -= a[start]

sys.stdout.write(str(maxSum))