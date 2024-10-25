import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = input().strip()
    start, end = 0, len(word)-1
    result = 0
    leftCheck, rightCheck = 0, 0

    while start < end:
        if word[start] != word[end]:
            s, e = start + 1, end
            while s < e:
                if word[s] != word[e]:
                    leftCheck = 1
                    break
                s += 1
                e -= 1

            s, e = start, end - 1
            while s < e:
                if word[s] != word[e]:
                    rightCheck = 1
                    break
                s += 1
                e -= 1

            if leftCheck == 0 or rightCheck == 0:
                result = 1
            else:
                result = 2
            break

        start += 1
        end -= 1

    sys.stdout.write(str(result)+'\n')