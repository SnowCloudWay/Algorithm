import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    sys.stdout.write(s[:1].upper() + s[1:]+'\n')
