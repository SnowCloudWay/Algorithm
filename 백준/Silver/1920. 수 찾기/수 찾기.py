import sys
input = sys.stdin.readline

n = int(input())
s = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in s:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')