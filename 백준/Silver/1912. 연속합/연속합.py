import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for i in range(n)]

for i in range(n):
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])

sys.stdout.write(str(max(dp)))