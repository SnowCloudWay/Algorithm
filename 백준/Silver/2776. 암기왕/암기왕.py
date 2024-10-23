import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    s = set(map(int, input().split()))
    M = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if num in s:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')