if __name__ == '__main__':
    K = int(input())
    s = []
    for _ in range(K):
        num = int(input())
        if num == 0:
            s.pop()
        else:
            s.append(num)
    print(sum(s))