# dictionary= ключ+значение
alphabet = {
    1: "A",
    2: "B",
    3: "C",
    4: {
        1: 'A',
        2: 3,
        3: {
            1: 'F',
            2: 'G',
        }
        },
    10: "Y",
    'Z': 10, #можно только ключи которые можно захешировать (list или touple нельзя туда)

}
# print(alphabet[1])
# print(alphabet[5]) # KeyError: 5 нет такого значения

# for pair in alphabet:  #только ключи
#     print(pair)
#
# for pair in alphabet.values():  #только значения
#     print(pair)
#
# for pair in alphabet.items():  #keys и values
#     print(pair)

for key, value in alphabet.items():  #keys и values
    if value in 'AY': #if value is A or Y
        print(f'Key {key} Значение {value}')

# _letter = alphabet.get('K', None) #вытаскиевает значение 10 если не находит пишет none
# if not bool(_letter):
#     print('No 0')


print(alphabet.get(4).get(3).get(1))

