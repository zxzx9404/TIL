case_num = int(input())
list_acc = []
for i in range(case_num):
    a = b = c = d = 0
    a, b, c, d = map(int, input().split())
    temp_list = []
    for j in range(c, 0, -1):
        for k in range(d, 0, -1):
            temp_list.append([j+a-1, k+b-1])
    list_acc.append(temp_list)

for m in range(case_num):
    for n in range(len(list_acc[m])):
        if












'''
[[1, 2], [3, 4], [5, 6], [7, 8]]



'''
