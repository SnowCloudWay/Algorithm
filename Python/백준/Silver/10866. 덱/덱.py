import sys
from collections import deque
input = sys.stdin.readline

dq = deque()

N = int(input())
for _ in range(N):
    command = list(map(str, input().split()))

    match command[0]:
        case "push_front":
            dq.appendleft(command[1])
        case "push_back":
            dq.append(command[1])
        case "pop_front":
            if len(dq) != 0:
                print(dq.popleft())
            else:
                print(-1)
        case "pop_back":
            if len(dq) != 0:
                print(dq.pop())
            else:
                print(-1)
        case "size":
            print(len(dq))
        case "empty":
            if len(dq) != 0:
                print(0)
            else:
                print(1)
        case "front":
            if len(dq) != 0:
                print(dq[0])
            else:
                print(-1)
        case "back":
            if len(dq) != 0:
                print(dq[-1])
            else:
                print(-1)