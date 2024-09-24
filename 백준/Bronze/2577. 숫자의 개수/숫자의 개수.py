if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    num = a * b * c

    num_list = list(map(int, str(num)))

    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in num_list:
        if i == 0:
            result[0] += 1
        elif i == 1:
            result[1] += 1
        elif i == 2:
            result[2] += 1
        elif i == 3:
            result[3] += 1
        elif i == 4:
            result[4] += 1
        elif i == 5:
            result[5] += 1
        elif i == 6:
            result[6] += 1
        elif i == 7:
            result[7] += 1
        elif i == 8:
            result[8] += 1
        elif i == 9:
            result[9] += 1

    for j in result:
        print(j)