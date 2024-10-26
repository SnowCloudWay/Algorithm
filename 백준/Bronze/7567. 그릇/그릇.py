import sys
input = sys.stdin.readline

dish = "d" + input().strip()
cm = 0

for i in range(1, len(dish)):
    if dish[i] != dish[i-1]:
        cm += 10
    else:
        cm += 5

sys.stdout.write(str(cm))