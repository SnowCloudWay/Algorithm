import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
