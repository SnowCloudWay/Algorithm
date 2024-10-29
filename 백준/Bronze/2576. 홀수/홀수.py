import sys
input = sys.stdin.readline

odd_nums = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        odd_nums.append(num)
if len(odd_nums) != 0:
    sys.stdout.write(str(sum(odd_nums)) + '\n')
    sys.stdout.write((str(min(odd_nums))))
else:
    sys.stdout.write(str(-1))