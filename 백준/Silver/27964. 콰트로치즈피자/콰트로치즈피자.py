import sys
input = sys.stdin.readline

cheese_topping = set()
n = int(input())
topping = list(map(str, input().split()))

for t in topping:
    if t[-6:].find("Cheese") != -1:
        cheese_topping.add(t)

if len(cheese_topping) >= 4:
    sys.stdout.write('yummy')
else:
    sys.stdout.write('sad')