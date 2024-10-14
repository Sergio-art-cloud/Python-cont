# a1 = int(input())
# a2 = float(input())
# a3 = input()
# a4 = float(input())
# list1 = [a1,a2,a3,a4]
#
# all_floats = True
# for item in list1:
#     if not isinstance(item,float):
#         all_floats = False
#         break
# print(all_floats)
#
# string_one = False
# for char in list1:
#     if isinstance(char,str):
#         string_one = True
#         break
# print(string_one)
#
# pairs = []
# for i in list1:
#     if isinstance(i, (int,float)):
#         str_i = str(i)
#     if len(str(i)) > 4:
#         pairs.append((str(i)[0],str(i)[2]))
#     if len(str(i)) > 1:
#         pairs.append((str(i)[1],str(i)[4]))
#     if len(str(i)) > 3:
#         pairs.append((str(i)[3],str(i)[4]))
#
# integer_pair = False
# for inter1,inter2 in list1:
#     if isinstance(inter1,int) and isinstance(inter2,int):
#         integer_pair = True
#         break
#
# print(integer_pair)