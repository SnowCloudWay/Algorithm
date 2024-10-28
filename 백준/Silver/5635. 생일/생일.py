import sys
input = sys.stdin.readline

students = []

n = int(input())
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    students.append([name, int(yyyy), int(mm), int(dd)])

s_students = list(sorted(students, key=lambda x:(x[1], x[2], x[3])))
sys.stdout.write(s_students[-1][0]+'\n')
sys.stdout.write(s_students[0][0])
