if __name__ == '__main__':
    a = int(input())
    b = int(input())

    b100 = b // 100
    b10 = b % 100 // 10
    b1 = b % 10

    print(a * b1)
    print(a * b10)
    print(a * b100)
    print(a * b)