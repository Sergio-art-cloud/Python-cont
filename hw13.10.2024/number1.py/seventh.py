num = int(input())
str_num = str(num)
count = []
for i in str_num:
    square = int(i) ** 2
    count.append(square)
print(sum(count))