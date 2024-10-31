import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
heap = []

nums = list(map(int, input().split()))
for num in nums:
    heapq.heappush(heap, num)

for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = a + b
    for _ in range(2):
        heapq.heappush(heap, c)

sys.stdout.write(str(sum(heap)))