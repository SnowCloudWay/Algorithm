import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
cnt = 0

for i in range(N):
    num = A[i]
    start, end = 0, N - 1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        if A[start] + A[end] == num:
            cnt += 1
            break
        elif A[start] + A[end] > num:
            end -= 1
        else:
            start += 1

sys.stdout.write(str(cnt))