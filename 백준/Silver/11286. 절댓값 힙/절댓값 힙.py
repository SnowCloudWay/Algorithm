import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write(str(heapq.heappop(heap)[1])+'\n')
    else:
        heapq.heappush(heap, (abs(num), num))