import sys, heapq
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)

sys.stdout.write(str(heapq.heappop(heap)))