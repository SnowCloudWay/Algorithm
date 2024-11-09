import sys
input = sys.stdin.readline

n = int(input())
aList = list(map(int, input().split()))
jun = aList[0]
live = True

aList[1:] = sorted(aList[1:])

for i in range(1, n):
    a = aList[i]
    if jun > a:
        jun += a
    else:
        live = False
        break

print("Yes" if live else "No")