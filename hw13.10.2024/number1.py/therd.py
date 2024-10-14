




temperature_of_days = {'first':18,'second':15,'therd':35}

sorted_temperature = dict(sorted(temperature_of_days.items(),key=lambda item: item[1]))
sorted_temperature_revice = dict(sorted(temperature_of_days.items(),key=lambda item: item[1],reverse=True))

print(sorted_temperature)
print(sorted_temperature_revice)