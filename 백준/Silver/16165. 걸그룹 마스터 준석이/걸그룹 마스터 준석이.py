import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
d = defaultdict(list)

for _ in range(n):
    name = input().strip()
    members = int(input())
    for _ in range(members):
        d[name].append(input().strip())
    d[name].sort()

for _ in range(m):
        name = input().strip()
        quiz = int(input().strip())
        if quiz == 0:
            for value in d[name]:
                sys.stdout.write(value+'\n')
        else:
            for key, values in d.items():
                if name in values:
                    sys.stdout.write(key+'\n')