import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
d = defaultdict(int)
for card in cards:
    d[card] += 1

m = int(input())
check = list(map(int, input().split()))
l = []
for c in check:
    l.append(d[c])
print(*l)