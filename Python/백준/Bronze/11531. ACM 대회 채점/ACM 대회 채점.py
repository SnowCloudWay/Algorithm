import sys
input = sys.stdin.readline

d = {}

sp, penalty = 0, 0

while True:
    log = input().split()
    if int(log[0]) == -1:
        break
    if log[2] == "right":
        if log[1] in d:
            penalty += d[log[1]] * 20
        penalty += int(log[0])
        sp += 1
    else:
        if log[1] in d:
            d[log[1]] += 1
        else:
            d[log[1]] = 1

print(sp, penalty)