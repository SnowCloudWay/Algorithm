import sys, heapq
input = sys.stdin.readline

heap = []
n = int(input())
l = []

for _ in range(n):
    start, end = map(int, input().split())
    l.append([start, end])

l.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    start, end = l[i]
    if heap and start >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

sys.stdout.write(str(len(heap)))