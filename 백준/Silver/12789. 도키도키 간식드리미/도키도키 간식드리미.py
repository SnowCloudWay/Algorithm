import sys

N = int(sys.stdin.readline().rstrip())
waiting = list(map(int, sys.stdin.readline().rstrip().split(" ")))
stack = []
num = 1

while True:
    if len(waiting) == 0 and len(stack) == 0:
        sys.stdout.write("Nice")
        break

    if len(waiting) == 0 and len(stack) != 0 and stack[-1] != num:
        sys.stdout.write("Sad")
        break

    if stack and stack[-1] == num:
        stack.pop()
        num += 1
    else:
        if waiting[0] == num:
            waiting.pop(0)
            num += 1
        else:
            stack.append(waiting.pop(0))