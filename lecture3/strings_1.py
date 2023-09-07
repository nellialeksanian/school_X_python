import string #библиотеа
#pip install
#local

# new_name: str = input("enter name")
# greet_messege = 'hello, bob'

#print(greet_messege[-3:]) #bob

# greet_messege: str = (
#     greet_messege [:-3] + new_name #:-3 до боба
# )

# greet_messege: str = greet_messege.replace('bob', new_name) #заменяет все вхождение боба, при этом возвращает измененную копию, а не меняет переменную
# print(greet_messege)

river: str = 'mmississippi'
# print(
#     river.lstrip('misp')) #удаляет все буквы которые он видит слева пока не увидит тот, который не подходит
#
# print(
#     river.rstrip('ppi')) #удаляет все буквы которые он видит справа пока не увидит тот, который не подходит

# word: str = '<!--- dsa das das----!>'
# print(word.strip('<!>-').split()) #strip удаляет нежелательные символы, split разделяет слова



# numbers: str = string.digits
# # print(numbers)
# word: str = 'hell123o you674'
# # for number in numbers: #цикл по numbers (перебераем цифры)
# #     word = word.replace(number, '')
# # #print(word)
#
# _word: str = ''
# for ch in word: #цикл чере word (перебираем буквы)
#     if ch in numbers:
#         continue
#     else:
#         _word+=ch
# word = _word
# print(word)

#Пустые переменные
# _word: str = ''
# _sum: float = 0.
# _prod: float = 1.
# _list: list = []
# _set: set = ([])
# _dict: dict = {}

words: str = 'hello Bob, are you a bob? BOB!!!'
# print(words.capitalize()) #fisrst letter is capitlized
# print(words.casefold())#all letters are small
#words = words.lower().replace('bob','greg')
#words = words.lower().find('bob')


while True:
    bob_index = words.lower().find('bob')
    if bob_index == -1:
        break
    else:
        words = (
                words[:bob_index] + #до начала 6 (индекса боба)
                'Gregory' +
                words[bob_index + len('bob'):] #боб_индекс это индекс боба + 3 длина боба то еть вмы так вычлиняем боба зная его позицию и длину
        )
        print(words, len('bob'))
        break
