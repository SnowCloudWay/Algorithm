import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = sorted(list(map(int, input().split())))
start, end = 0, N-1
cnt = 0

if N > 1:
    while start < end:
        if a[start] + a[end] >= M:
            cnt += 1
            start += 1
            end -= 1
        elif a[start] + a[end] < M:
            start += 1

sys.stdout.write(str(cnt)+'\n')