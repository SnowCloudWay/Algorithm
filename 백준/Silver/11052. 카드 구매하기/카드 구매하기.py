import sys

N = int(sys.stdin.readline().rstrip())
P = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * (N + 1)

dp[1] = P[1]

for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i - j] + P[j]:
            dp[i] = dp[i-j] + P[j]
        # dp[i] = max(dp[i], P[j] + dp[i-j])

sys.stdout.write(str(dp[N]))