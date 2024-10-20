import sys
input = sys.stdin.readline

winner = 0
maxScore = 0

for i in range(1, 6):
    score = list(map(int, input().split()))
    totalScore = sum(score)
    if maxScore < totalScore:
        maxScore = totalScore
        winner = i

sys.stdout.write(str(winner) + ' ' + str(maxScore))