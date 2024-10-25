import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
intervalSumList = [sum(nums[:k])]

for i in range(n - k):
    intervalSum = intervalSumList[i] - nums[i] + nums[i+k]
    intervalSumList.append(intervalSum)

sys.stdout.write(str(max(intervalSumList)))