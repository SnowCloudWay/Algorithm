import sys

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        L = sys.stdin.readline().rstrip()
        left_pw = []
        right_pw = []
        for i in L:
            if i == '<' and left_pw:
                right_pw.append(left_pw.pop())
            elif i == '>' and right_pw:
                left_pw.append(right_pw.pop())
            elif i == '-' and left_pw:
                left_pw.pop()
            elif i not in "<>-":
                left_pw.append(i)
        password = ''.join(left_pw + right_pw[::-1])
        print(password)