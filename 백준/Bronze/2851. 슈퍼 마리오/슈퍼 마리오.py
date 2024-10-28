import sys
input = sys.stdin.readline

prefix_sum = [int(input())]

for i in range(1, 10):
    prefix_sum.append(prefix_sum[i-1] + int(input()))
    if prefix_sum[i] >= 100:
        break

if prefix_sum[-1] == 100:
    sys.stdout.write(str(100))
else:
    l = 100 - prefix_sum[-2]
    r = prefix_sum[-1] - 100
    if l < r:
        sys.stdout.write(str(prefix_sum[-2]))
    else:
        sys.stdout.write(str(prefix_sum[-1]))