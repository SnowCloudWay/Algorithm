import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    a_idx, b_idx = 0, 0
    cnt = 0
    while a_idx < N and b_idx < M:
        if A[a_idx] > B[b_idx]:
            cnt += N - a_idx
            b_idx += 1
        else:
            a_idx += 1

    sys.stdout.write(str(cnt)+'\n')