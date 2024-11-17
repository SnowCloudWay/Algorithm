import sys
input = sys.stdin.readline

totalSum = 0

while True:
    num = int(input())
    if num == -1:
        break
    totalSum += num

print(totalSum)