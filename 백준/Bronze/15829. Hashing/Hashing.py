import sys

L = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
r = 31
M = 1234567891
n = 0
result = 0

for i in s:
    result += (ord(i) - 96) * (r ** n)
    n += 1

result = result % M

sys.stdout.write(str(result))