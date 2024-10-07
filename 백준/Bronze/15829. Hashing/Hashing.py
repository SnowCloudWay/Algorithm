import sys

L = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
M = 31
n = 0
result = 0

for i in s:
    result += (ord(i) - 96) * (M ** n)
    n += 1

sys.stdout.write(str(result))