import sys
from collections import OrderedDict
input = sys.stdin.readline

k, l = map(int, input().split())
o_dict = OrderedDict()

for _ in range(l):
    num = input().strip()
    if num in o_dict:
        o_dict.pop(num)
        o_dict[num] = 0
    else:
        o_dict[num] = 0

for i, (key, value) in enumerate(o_dict.items()):
    if i >= k:
        break
    sys.stdout.write(str(key)+'\n')