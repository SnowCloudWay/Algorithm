import sys
input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))
sumTime = 0
totalTime = times[0]

for i in range(1, n):
    sumTime += times[i-1]
    totalTime += sumTime + times[i]

sys.stdout.write(str(totalTime))