import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dq = deque(i for i in range(1, n+1))
cnt = 0

for num in nums:
    while True:
        if num == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(num) > len(dq) // 2:
                dq.rotate(1)
                cnt += 1
            else:
                dq.rotate(-1)
                cnt += 1

sys.stdout.write(str(cnt))

