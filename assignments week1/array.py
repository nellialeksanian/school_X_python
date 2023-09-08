_list = [int(value) for value in input('Введите числа через пробел: ').split()]
_newlist = []

for i in range(len(_list)):
    if _list[i] - _list[i - 1] > 1:
        _newlist.append(i)

if len(_newlist) == 0:
    print('Не найдено')
elif len(_newlist) == 1:
    print(_newlist[0])
else:
    print(_newlist)




