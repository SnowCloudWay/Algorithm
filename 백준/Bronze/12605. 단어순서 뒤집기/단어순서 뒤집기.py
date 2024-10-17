import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    word = list(map(str, sys.stdin.readline().rstrip().split()))
    print('Case #{}:'.format(i), ' '.join(word[::-1]).format(i))