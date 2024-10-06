import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    basket[i-1:j] = basket[i-1:j][::-1]

sys.stdout.write(' '.join(map(str, basket)))