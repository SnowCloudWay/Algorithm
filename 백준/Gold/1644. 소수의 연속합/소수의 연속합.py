import sys
input = sys.stdin.readline

n = int(input())
primeNums = []
intervalSum = 0
end = 0
cnt = 0

# 에라토스테네스의 체
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
primeNums = [i for i, prime in enumerate(is_prime) if prime]

primeNumsLen = len(primeNums)
for start in range(primeNumsLen):
    while intervalSum < n and end < primeNumsLen:
        intervalSum += primeNums[end]
        end += 1
    if intervalSum == n:
        cnt += 1
    intervalSum -= primeNums[start]

sys.stdout.write(str(cnt))