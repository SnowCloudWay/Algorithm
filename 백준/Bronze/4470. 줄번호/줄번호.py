if __name__ == '__main__':
    n = int(input())
    strList = []

    for i in range(n):
        strList.append(str(i+1) + ". " + input())

    for j in strList:
        print(j)