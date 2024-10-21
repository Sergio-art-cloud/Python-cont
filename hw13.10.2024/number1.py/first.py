count = 0
def Print(sentence):
    global count
    count += 1
    print(f'{count}: {sentence}')

# def Print(sentence, count=0):
#     count += 1
#     print(f'{count}: {sentence}')
#     return count

Print('hi how are you?')
Print('hi how are you?')
Print('hi how are you?')
