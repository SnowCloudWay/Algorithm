import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
prefix_sum[1] = a[0]
for i in range(1, n):
    prefix_sum[i+1] = prefix_sum[i] + a[i]

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    sys.stdout.write(str(prefix_sum[j] - prefix_sum[i-1]) + '\n')