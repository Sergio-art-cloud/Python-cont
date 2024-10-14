list1 = [0.3,False,None,True,'sound','pencel','book',8,5.55]
string_list1 = []
for item in list1:
    if isinstance(item,str):
        string_list1.append(item)
print(string_list1)
filter_bool = [item for item in list1 if isinstance(item,bool)]
print(filter_bool)