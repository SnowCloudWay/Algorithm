if __name__ == '__main__':
    t = 0
    for _ in range(4):
        t += (int(input()))
    x = t // 60
    y = t % 60
    print(x)
    print(y)