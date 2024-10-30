import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, sys.stdin.read().splitlines())))

answer = max(nums) - min(nums)
start = 0
end = 0

while start < n - 1:
    result = nums[end] - nums[start]
    if result >= m:
        if answer > result:
            answer = result
        start += 1
    else:
        if end < n - 1:
            end += 1
        else:
            start += 1

sys.stdout.write(str(answer))