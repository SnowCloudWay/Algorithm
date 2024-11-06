import sys
from collections import Counter
input = sys.stdin.readline

number = {'Z':[0, 'ZERO'],
          'W':[2, 'TWO'],
          'U':[4, 'FOUR'],
          'X':[6, 'SIX'],
          'G':[8, 'EIGHT'],
          'O':[1, 'ONE'],
          'H':[3, 'THREE'],
          'F':[5, 'FIVE'],
          'S':[7, 'SEVEN'],
          'I':[9, "NINE"]}
number_a = ['Z', 'W', 'U', 'X', 'G', 'O', 'H', 'F', 'S', 'I']

t = int(input())

for i in range(t):
    s = input().strip()
    count = Counter(s)
    result = []

    for k in number_a:
        num, word = number[k]
        cnt = count[k]
        if cnt > 0:
            result.extend([num] * cnt)
            for w in word:
                count[w] -= cnt
    result.sort()
    print("Case #{}: ".format(i+1) + ''.join(map(str, result)))