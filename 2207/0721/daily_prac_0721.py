old_list = [1, 1, 3, 3, 0, 1, 1]
new_list = [old_list[0]]

for i in range(1, len(old_list)):
    if old_list[i] != new_list[len(new_list)-1]:
        new_list.append(old_list[i])

print(new_list)


#교수님 풀이

'''
numbers = [1, 1, 3, 3, 0, 1, 1]
result = []

for idx, num in enumerate(numbers):
    if idx == 0 or result[-1] != num:
        result.append(num)
print(num)
'''