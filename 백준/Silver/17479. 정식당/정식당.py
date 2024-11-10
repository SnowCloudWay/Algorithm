import sys
input = sys.stdin.readline

menuN, menuS = {}, {}
service = []
serviceCnt = 0
menuNPrice, menuSPrice = 0, 0

a, b, c = map(int, input().split())

for _ in range(a):
    menu, price = input().split()
    menuN[menu] = int(price)

for _ in range(b):
    menu, price = input().split()
    menuS[menu] = int(price)

for _ in range(c):
    service.append(input().strip())

for _ in range(int(input())):
    menu = input().strip()
    if menu in menuN:
        menuNPrice += menuN[menu]
    elif menu in menuS:
        menuSPrice += menuS[menu]
    else:
        serviceCnt += 1

if menuNPrice < 20000 and menuSPrice != 0 or menuSPrice + menuNPrice < 50000 and serviceCnt != 0 or serviceCnt > 1:
    sys.stdout.write("No")
else:
    sys.stdout.write("Okay")