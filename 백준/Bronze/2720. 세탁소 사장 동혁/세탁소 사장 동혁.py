import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c = int(input())
    l = [0,0,0,0]
    while c != 0:
        if c // 25 >= 1:
            l[0] += c // 25
            c = c % 25
        if c // 10 >= 1:
            l[1] += c // 10
            c = c % 10
        if c // 5 >= 1:
            l[2] += c // 5
            c = c % 5
        l[3] = c
        break
    print(*l)