import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
prefix_sum[1] = nums[0]
for i in range(1, n):
    prefix_sum[i+1] = prefix_sum[i] + nums[i]

for _ in range(m):
    i, j = map(int, input().split())
    result = prefix_sum[j] - prefix_sum[i-1]
    sys.stdout.write(str(result)+'\n')