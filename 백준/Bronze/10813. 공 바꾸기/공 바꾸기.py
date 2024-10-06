import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
balls = [str(i) for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    temp = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j-1] = temp

print(' '.join(balls))