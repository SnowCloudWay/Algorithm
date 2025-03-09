import sys
from queue import Queue
input = sys.stdin.readline

N = int(input())
que = Queue()

for _ in range(N):
    command = list(map(str, input().split()))

    match command[0]:
        case "push":
            que.put(command[1])
        case "pop":
            if que.qsize() != 0:
                print(que.get())
            else:
                print(-1)
        case "size":
            print(que.qsize())
        case "empty":
            if que.qsize() != 0:
                print(0)
            else:
                print(1)
        case "front":
            if que.qsize() != 0:
                print(que.queue[0])
            else:
                print(-1)
        case "back":
            if que.qsize() != 0:
                print(que.queue[-1])
            else:
                print(-1)