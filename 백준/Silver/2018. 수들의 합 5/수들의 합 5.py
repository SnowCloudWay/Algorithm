import sys

n = int(sys.stdin.readline())

sum = 1
start = 1
end = 1
cnt = 1

while end < n:
    if sum == n:
        cnt += 1
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

sys.stdout.write(str(cnt))