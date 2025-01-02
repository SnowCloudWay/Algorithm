import sys
input = sys.stdin.readline

while(True):
    pw = input().strip()
    flag = False
    aeiou = 0
    acnt = 0
    bcnt = 0
    lp = 'A'

    if pw == "end":
        break

    for p in pw:
        if p in "aeiou":
            aeiou += 1
        if lp == p and p != 'e' and p != 'o':
            flag = True
            break
        if p in "aeiou":
            acnt += 1
            bcnt = 0
        else:
            bcnt += 1
            acnt = 0
        if acnt >= 3 or bcnt >= 3:
            flag = True
            break
        lp = p

    if flag == False and aeiou >= 1:
        sys.stdout.write(f'<{pw}> is acceptable.\n')
    else:
        sys.stdout.write(f'<{pw}> is not acceptable.\n')
