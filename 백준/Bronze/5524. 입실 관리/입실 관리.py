if __name__ == '__main__':
    n = int(input())
    checkInList = []
    for i in range(0, n):
        checkInList.append(input().lower())
    for people in checkInList:
        print(people)