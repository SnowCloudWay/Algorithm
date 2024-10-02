if __name__ == '__main__':
    K = int(input())
    s = []
    result = 0
    for _ in range(K):
        num = int(input())
        if num != 0:
            s.append(num)
        elif num == 0:
            s.pop()
    print(sum(s))