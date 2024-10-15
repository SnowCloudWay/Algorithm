import sys

n, m = map(int, sys.stdin.readline().split())
a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]
result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    b[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        result[i][j] += a[i][j] + b[i][j]

for i in result:
    for j in i:
        print(j, end=' ')
    print()