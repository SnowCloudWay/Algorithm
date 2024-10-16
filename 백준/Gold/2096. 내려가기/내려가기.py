import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

maxDp = nums
minDp = nums

for _ in range(n-1):
    nums = list(map(int, sys.stdin.readline().split()))
    maxDp = [max(maxDp[0], maxDp[1]) + nums[0], max(maxDp[0], maxDp[1], maxDp[2]) + nums[1], max(maxDp[1], maxDp[2]) + nums[2]]
    minDp = [min(minDp[0], minDp[1]) + nums[0], min(minDp[0], minDp[1], minDp[2]) + nums[1], min(minDp[1], minDp[2]) + nums[2]]

print(max(maxDp), min(minDp))