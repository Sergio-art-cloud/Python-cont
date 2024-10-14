list1 = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
for index, value in enumerate(list1,start=1):
    if index - 1 < len(value):
        char = value[index-1]
    else:
        char = None
    print(f'{index} - {value} - {char}')