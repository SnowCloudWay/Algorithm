import sys
from collections import deque
input = sys.stdin.readline

dq = deque()

n = int(input())
dqMaxLen = 0
lastStudent = n+1

for i in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        dq.append(command[1])

        dqLen = len(dq)
        if dqMaxLen <= dqLen:
            if dqMaxLen == dqLen:
                if lastStudent > dq[-1]:
                    lastStudent = dq[-1]
            else:
                dqMaxLen = dqLen
                lastStudent = dq[-1]
    else:
        dq.popleft()

sys.stdout.write(str(dqMaxLen) + " " + str(lastStudent))