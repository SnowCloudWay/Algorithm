import sys
input = sys.stdin.readline

l = [[] for _ in range(6)]
cnt = 0
n, p = map(int, input().split())

read = sys.stdin.read().splitlines()
for r in read:
    a, b = map(int, r.split())
    a -= 1
    if len(l[a]) == 0:
        l[a].append(b)
        cnt += 1
    else:
        if l[a][-1] < b:
            l[a].append(b)
            cnt += 1
        elif l[a][-1] > b:
            while True:
                if len(l[a]) == 0 or l[a][-1] <= b:
                    break
                l[a].pop()
                cnt += 1
            if len(l[a]) == 0 or l[a][-1] < b:
                l[a].append(b)
                cnt += 1

print(cnt)