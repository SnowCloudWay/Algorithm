import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = sorted(list(map(int, input().split())))
start, end = 0, n - 1
intervalSum = 0
cnt = 0

while start < end:
    intervalSum = nums[start] + nums[end]
    if intervalSum == m:
        cnt += 1
        start += 1
        end -= 1
    elif intervalSum < m:
        start += 1
    else:
        end -= 1
sys.stdout.write(str(cnt))