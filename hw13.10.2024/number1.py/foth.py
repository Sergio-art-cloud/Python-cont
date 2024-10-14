import copy

list1 = [1,2,3,4,5,6,7,8,9]
copy_list1 = list1.copy()
copy_list2 = list1[:]
copy_list3 = copy.deepcopy(list1)

vtoria_stepen = list(map(lambda x: x ** 2, list1 ))
print(vtoria_stepen)


list2 = list(map(lambda x: x + 3 if x % 2 == 0 else x, list1))
print(list2)

list3 = list(filter(lambda x: x * 2 if x % 2 == 0 else x,
                    filter(lambda x: x % 2 == 0, list1)))
print(list3)

list4 = list(map(lambda x: x * 3 if x % 2 != 0 else x, filter(lambda x: x % 2 != 0, list1)))
print(list4)

count_mult_too = []
count_mult_tree = []
for i in range(len(list1)):
    if i % 2 == 0:
        count_mult_too.append(i*2)
    if i % 2 != 0:
        count_mult_tree.append(i*3)

print(count_mult_too)
print(count_mult_tree)