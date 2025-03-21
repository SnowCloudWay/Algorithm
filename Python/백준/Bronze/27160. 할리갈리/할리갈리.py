import sys
input = sys.stdin.readline

d = {"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}
bell = False

N = int(input())

for i in range(N):
    fruit, num = map(str, input().split())
    d[fruit] += int(num)

for v in d.values():
    if v == 5:
        bell = True
        break

print("YES" if bell else "NO")