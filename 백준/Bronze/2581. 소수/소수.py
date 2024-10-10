import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
L = []

for num in range(M, N+1):
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
                break
        if cnt == 0:
            L.append(num)

if len(L) > 0:
    sys.stdout.write(str(sum(L))+"\n")
    sys.stdout.write(str(min(L)))
else:
    sys.stdout.write(str(-1))