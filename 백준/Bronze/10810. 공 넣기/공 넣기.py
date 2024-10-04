import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
balls = [0 for b in range(N)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for idx in range(i-1, j):
        balls[idx] = k

print(' '.join(map(str, balls)))