if __name__ == '__main__':
    n = int(input())
    members = [[0 for j in range(2)] for i in range(n)]
    for i in range(0, n):
        age, name = input().split()
        members[i][0] = int(age)
        members[i][1] = name
    members.sort(key=lambda x: x[0])
    for member in members:
        print(member[0], member[1])