# all = []
# for _ in range(int(input())):
#     student = []
#     name = input()
#     score = float(input())
#     student.append(name)
#     student.append(score)
#     all.append(student)
# all.sort()
# all.sort(key = lambda x : x[1])
# print("ALL",all)
# for i in all:
#     if all[1][1] in i:
#         print("Got it",i)


all = []
for _ in range(int(input())):
    student = []
    name = input()
    score = float(input())
    student.append(name)
    student.append(score)
    all.append(student)
all.sort()
all.sort(key = lambda x : x[1])
get = (len([i for i in all if all[0][1] == i[1]]))
for i in all:
    if all[get][1] in i:
        print(i[0])