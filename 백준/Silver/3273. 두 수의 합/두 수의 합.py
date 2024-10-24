import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
start = 0
end = n - 1
cnt = 0

while start < end:
    sum = nums[start] + nums[end]

    if sum == x:
        cnt += 1
        start += 1
    elif sum < x:
        start += 1
    else:
        end -= 1

sys.stdout.write(str(cnt))