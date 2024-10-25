import sys
input = sys.stdin.readline

def solution(N, X, views):
    interval_sum = sum(views[:X])
    max_views = interval_sum
    cnt = 0
    if max_views != 0:
        cnt = 1
    start, end = 0, X

    while end < N:
        interval_sum -= views[start]
        interval_sum += views[end]
        start += 1
        end += 1
        if interval_sum == max_views:
            cnt += 1
        elif interval_sum > max_views:
            max_views = interval_sum
            cnt = 1

    return max_views, cnt


N, X = map(int, input().split())
views = list(map(int, input().split()))

result1, result2 = solution(N, X, views)
if result1 == 0:
    sys.stdout.write("SAD")
else:
    sys.stdout.write(str(result1)+'\n')
    sys.stdout.write(str(result2)+'\n')