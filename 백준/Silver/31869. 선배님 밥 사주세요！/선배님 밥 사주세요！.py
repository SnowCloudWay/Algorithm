import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
max_cnt = 0
data = {}
data2 = {}
day = [[False for _ in range(7)] for _ in range(10)]

for _ in range(n):
    s, w, d, p = map(str, input().split())
    data[s] = [int(w), int(d), int(p)]

sorted_data = dict(sorted(data.items(), key=lambda item:(item[1][0], item[1][1])))

for _ in range(n):
    name, m = map(str, input().split())
    data2[name] = int(m)

for s, wdp in sorted_data.items():
    if data2.get(s, 0) >= wdp[2]:
        day[wdp[0]-1][wdp[1]] = True

for i in range(10):
    for j in range(7):
        if day[i][j]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)

sys.stdout.write(str(max_cnt))