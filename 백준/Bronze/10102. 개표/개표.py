import sys
from collections import Counter
input = sys.stdin.readline

v = int(input())
s = input().strip()
counter = Counter(s)

cntA = counter["A"]
cntB = counter["B"]

if cntA > cntB:
    sys.stdout.write("A")
elif cntA < cntB:
    sys.stdout.write("B")
else:
    sys.stdout.write("Tie")