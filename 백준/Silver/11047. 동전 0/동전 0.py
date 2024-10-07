import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = []
cnt = 0

for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

for c in coins[::-1]:
    if K == 0: break
    if K // c > 0:
        cnt += K // c
        K = K % c

sys.stdout.write(str(cnt))