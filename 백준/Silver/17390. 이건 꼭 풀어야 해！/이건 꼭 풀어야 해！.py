import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

s_arr = sorted(arr, key=lambda x: x)

prefix_sum = [0] * (n + 1)
prefix_sum[1] = s_arr[0]
for i in range(1, n):
    prefix_sum[i+1] = prefix_sum[i] + s_arr[i]

for _ in range(q):
    l, r = map(int, input().split())
    sys.stdout.write(str(prefix_sum[r] - prefix_sum[l-1])+'\n')