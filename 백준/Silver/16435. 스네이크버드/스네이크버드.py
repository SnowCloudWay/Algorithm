import sys
input = sys.stdin.readline

N, l = map(int, input().split())
hList = sorted(list(map(int, input().split())))

for h in hList:
    if l >= h:
        l += 1
    else:
        break

sys.stdout.write(str(l))