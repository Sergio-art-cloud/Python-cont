def Users(**kwargs):
    FIO = []
    if 'name' in kwargs:
        FIO.append(kwargs['name'])
    if 'surname' in kwargs:
        FIO.append(kwargs['surname'])
    if 'age' in kwargs:
        FIO.append(str(kwargs['age']))

    if FIO:
        print(' '.join(FIO))
    else:
        print('Нужные данные отсутствуют')


Users(name='Sergio',surname='Daineka',age=51)