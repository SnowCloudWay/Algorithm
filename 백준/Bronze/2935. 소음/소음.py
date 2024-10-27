import sys

s = sys.stdin.read().splitlines()
ss = s[0]+s[1]+s[2]
print(eval(ss))