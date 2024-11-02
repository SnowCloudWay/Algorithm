import sys
input = sys.stdin.readline

students = []

n = int(input())
for _ in range(n):
    name, ko, en, ma = input().split()
    students.append([name, int(ko), int(en), int(ma)])

sortStudents = sorted(students, key=lambda x:(-x[1], x[2], -x[3], x[0]))
for student in sortStudents:
    sys.stdout.write(student[0]+'\n')