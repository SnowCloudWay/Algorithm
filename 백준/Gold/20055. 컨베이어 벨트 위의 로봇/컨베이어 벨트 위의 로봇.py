import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * n)
cnt = 0

while True:
    cnt += 1
    belt.rotate(1)
    robots.rotate(1)
    robots[n-1] = 0

    for i in range(n-2, -1, -1):
        if belt[i+1] >= 1 and robots[i+1] == 0 and robots[i] == 1:
            robots[i+1] = 1
            robots[i] = 0
            belt[i+1] -= 1
    robots[-1] = 0

    if belt[0] != 0 and robots[0] != 1:
        robots[0] = 1
        belt[0] -= 1

    if belt.count(0) >= k:
        sys.stdout.write(str(cnt))
        break