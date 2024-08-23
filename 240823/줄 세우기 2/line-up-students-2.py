n = int(input())
students = []
for number in range(n):
    height, weight = input().split()
    students.append((int(height), -int(weight), number+1))
students.sort()
for i in range(n):
    print(students[i][0], -students[i][1], students[i][2])