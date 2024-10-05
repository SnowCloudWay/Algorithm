import sys
from queue import Queue

N = int(sys.stdin.readline().rstrip())
que = Queue()

for i in range(N):
    que.put(i+1)

while True:
    if que.qsize() == 1:
        print(que.get())
        break
    que.get()
    que.put(que.get())