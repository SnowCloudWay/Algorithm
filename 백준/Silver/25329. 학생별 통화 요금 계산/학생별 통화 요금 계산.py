import sys, math
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)

n = int(input())
for _ in range(n):
    time, name = input().split()
    time1, time2 = map(int, time.split(':'))
    total_time = time2 + (time1 * 60)
    d[name] += total_time

for key, value in d.items():
    money = 10
    if value > 100:
        value = math.ceil((value - 100) / 50) * 3
        d[key] = money + value
    else:
        d[key] = money

s_d = dict(sorted(d.items(), key=lambda item:(-item[1], item[0])))
for key, value in s_d.items():
    sys.stdout.write(key + " " + str(value) + '\n')