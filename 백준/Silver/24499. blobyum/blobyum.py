import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = arr * 2

windowSum = sum(arr[i] for i in range(k))
maxApplePie = windowSum

for i in range(1, n):
    windowSum = windowSum - arr[i - 1] + arr[i + k - 1]
    maxApplePie = max(maxApplePie, windowSum)

sys.stdout.write(str(maxApplePie))