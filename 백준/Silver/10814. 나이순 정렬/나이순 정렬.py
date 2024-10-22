import sys
from collections import OrderedDict
input = sys.stdin.readline

od = OrderedDict()
n = int(input())

for i in range(n):
    info = list(map(str, input().split()))
    od[i] = [int(info[0]), info[1]]

sorted_od = OrderedDict(sorted(od.items(), key=lambda x: x[1][0]))

for k, v in sorted_od.items():
    sys.stdout.write(str(v[0])+' '+v[1]+'\n')