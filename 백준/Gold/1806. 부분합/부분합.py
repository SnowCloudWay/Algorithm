import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
intervalSum = 0
minLen = n
check = 0
end = 0

for start in range(n):
    while intervalSum < s and end < n:
        intervalSum += nums[end]
        end += 1
    if intervalSum >= s:
        minLen = min(minLen, end - start)
        check = 1
    intervalSum -= nums[start]

if check == 1:
    sys.stdout.write(str(minLen))
else:
    sys.stdout.write(str(0))