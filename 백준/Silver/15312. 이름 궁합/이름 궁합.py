import sys
input = sys.stdin.readline

alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input().strip()
b = input().strip()

l = []
for i in range(len(a)):
    l.append(alphabet[ord(a[i])-65])
    l.append(alphabet[ord(b[i])-65])

while len(l) != 2:
    l = [(l[i] + l[i+1]) % 10 for i in range(len(l)-1)]

sys.stdout.write(str(l[0]) + str(l[1]))