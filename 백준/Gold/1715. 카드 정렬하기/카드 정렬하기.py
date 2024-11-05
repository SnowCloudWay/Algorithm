import sys, heapq
input = sys.stdin.readline

heap = []
cnt = 0

n = int(input())
for _ in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    res = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, res)
    cnt += res

sys.stdout.write(str(cnt))