if __name__ == '__main__':
    n = int(input())
    coordinates = [[0 for j in range(2)] for i in range(n)]

    for c in range(0, n):
        x, y = map(int, input().split())
        coordinates[c][0] = x
        coordinates[c][1] = y

    coordinates.sort(key=lambda x: (x[0], x[1]))
    for coordinate in coordinates:
        print(coordinate[0], coordinate[1])