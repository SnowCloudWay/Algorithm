if __name__ == '__main__':
    l = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    ac = a // c
    if a % c != 0:
        ac += 1

    bd = b // d
    if b % d != 0:
        bd += 1

    funDay = l - max(ac, bd)
    print(funDay)