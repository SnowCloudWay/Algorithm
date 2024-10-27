import sys
input = sys.stdin.readline

s = input()
rot13 = []

for i in s:
    if "A" <= i <= 'Z':
        i =ord(i) + 13
        if i > ord('Z'):
            i -= 26
        rot13.append(chr(i))
    elif "a" <= i <= 'z':
        i = ord(i) + 13
        if i > ord('z'):
            i -= 26
        rot13.append(chr(i))
    else:
        rot13.append(i)

sys.stdout.write("".join(rot13))