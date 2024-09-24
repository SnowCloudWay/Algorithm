if __name__ == '__main__':
    max_num = 0
    max_n = 0
    for i in range(9):
        num = int(input())
        if num > max_num:
            max_num = num
            max_n = i + 1
    print(max_num)
    print(max_n)