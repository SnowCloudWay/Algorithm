import sys
input = sys.stdin.readline

s = set()
pw = ""

n = int(input())
for _ in range(n):
    word = input().strip()
    s.add(word)

for i in s:
    if i == i[::-1]:
        pw = i
        break
    elif i[::-1] in s:
        pw = i
        break

sys.stdout.write(str(len(pw)) + " " + str(pw[(len(pw) // 2)]))