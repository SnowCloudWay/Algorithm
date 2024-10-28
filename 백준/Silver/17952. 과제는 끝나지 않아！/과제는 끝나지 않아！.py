import sys
input = sys.stdin.readline

hw = []
score = 0

n = int(input())
for _ in range(n):
    command = list(map(int, input().split()))

    if command[0] == 1:
        if command[2] == 1:
            score += command[1]
        else:
            hw.append([command[1], command[2]-1])

    else:
        if hw:
            hw[-1][1] -= 1
            if hw[-1][1] == 0:
                score += hw[-1][0]
                hw.pop()

sys.stdout.write(str(score))