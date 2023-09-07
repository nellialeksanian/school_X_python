
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
print(_list1[1])
"""

numbers: list = [1,2,3,4,5,6,7,8,9,15]
# for n in numbers:
#     if n % 3 == 0:
#         print(f'число - {n} кратно 3')
#     if n % 3 != 0:
#         print(f'число - {n} не кратно 3')
# for n in numbers:
#     if n % 5 == 0 & n % 3 == 0: #большие условия должны быть выше
#         print(f'number {n} devides on 3 and 5')
#     elif n % 3 == 0:
#         print(f'число - {n} dev 3')
#     elif n % 5 == 0:        #если бы было if то на каждой итерации будет и первый if и второй. А так на первом if итерация заканчивается
#         print(f'число - {n} dev 5')
#     else:
#         print(f'number {n} doesnt devide on 3 щк on 5')

# word: str = input('введите слово')
# vowel: str = 'aeiouy'
# vowel_count: int = 0
# print(vowel[2])
# for char in word: #слово итериурется побуквенно
#     if char in vowel:
#         vowel_count += 1
# print(vowel_count)
#range(1, x+1, +2) +2 это шаг

#  задача матеша:
# x = int(input('введите число'))
# summa = 0
# for number in range(x+1):
#     if (number % 3 == 0 and not number % 5 == 0) or (not number % 3 == 0 and number % 5 == 0):
#        summa += number
# print(summa)

#     if number % 5 == 0 & number % 3 == 0: #большие условия должны быть выше
#         continue
#     elif number % 3 == 0:
#         list_3.append(i)
#     elif n % 5 == 0:        #если бы было if то на каждой итерации будет и первый if и второй. А так на первом if итерация заканчивается
#         list_5.append (i)
#       summ_total = sum(list_3)+sum(list_5)

n: int = int (input("enetr N"))
# while n > 0:
#     print(n)
#     n=n-1
i=0
should_braked: bool = False
array: list = list(range(1,n))
while True:
    if array[i] % 123 == 0:
        print(array[i], 'делиться')
        if should_braked:
            break #завершает while
        else:
            should_braked = True
    i+=1 #инткрементирует на 1 i = i+1 переназначает переменную (лучше использовать со сложными

