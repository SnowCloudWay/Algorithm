import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for i in range(1, n):
        if i == 1:
            dp[0][i] = dp[1][i - 1] + sticker[0][i]
            dp[1][i] = dp[0][i - 1] + sticker[1][i]
        else:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))