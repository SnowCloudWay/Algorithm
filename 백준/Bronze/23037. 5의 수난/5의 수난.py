import sys

num = sys.stdin.readline().rstrip()
result = 0

for i in range(5):
    result += int(num[i]) ** 5

print(result)