if __name__ == '__main__':
    a, b, c = map(int, input().split())

    t1 = (a + b) % c
    t2 = ((a % c) + (b % c)) % c
    t3 = (a * b) % c
    t4 = ((a % c) * (b % c)) % c
    print(t1)
    print(t2)
    print(t3)
    print(t4)