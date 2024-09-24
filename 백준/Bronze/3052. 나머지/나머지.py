if __name__ == '__main__':

    result1 = []
    result2 = []

    for _ in range(10):
        n = int(input())
        result1.append(n%42)

    for value in result1:
        if value not in result2:
            result2.append(value)

    print(len(result2))