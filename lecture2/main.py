"""
a,b,c = input('введите числa').split()
a,b,c = float(a), float(b), float(c)
z = a+b+c
y = a**b**c
print(a,b,c, sep=',')
print(z,y, sep='\n')


# print("Ты", "очень "*y, "крут")
"""

_list: list = [1,3,23,45,0,None,'sad',False]

_set3: set = {'m','i','s', 's'}
_set4: set = {'l', 's'}
print(_set3.intersection(_set4))
print(_set3.difference(_set4))


_list1=[1,2,3,4]
_list1.append(8)  #добавился элемент
_list1.append([5,6]) #добавился еще один лист
matrix = [[1,2],[2,5], [6,9]]
print(matrix[2][0]) #достаем 6 (первый элемент в третьем элементе)
print(_list1[])