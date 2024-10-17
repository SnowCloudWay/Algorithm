import sys
for i in range(1, int(sys.stdin.readline())+1):
    word = list(map(str, sys.stdin.readline().rstrip().split()))
    print('Case #{}:'.format(i), ' '.join(word[::-1]).format(i))