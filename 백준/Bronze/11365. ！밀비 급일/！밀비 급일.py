import sys
input = sys.stdin.readline

while(True):
    msg = input().strip()
    if msg == "END":
        break
    else:
        sys.stdout.write(msg[::-1]+'\n')