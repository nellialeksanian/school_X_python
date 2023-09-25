def convert_ab_to_int(a: str, b: str) -> tuple[int, int]:
    a, b = int(a), int(b)
    return a,b
def divide(a: int | float, b: int |float) -> float:
    if 3 in [a,b]:
        raise AttributeError("I hate 3")
    return a/b

while True: #программа рабоатет все время пока не будет ошибка
    a, b = input('Enter 2 numbers to find the sum:').split()
    try:
        a, b = convert_ab_to_int(a,b) #не перевелось в инт, но программа не сломалась и сложила 2 строки
        devision_score = divide(a, b)
    except (ValueError, ZeroDivisionError) as e: #exception все бызовые ошибки
        print(f'ошибка {e}')
        print('введите числа и без нулей')
        print()
        continue #чтобы заново вызвать while (программа на сломалась а просит вести цифры)
    except AttributeError as ex:
        print(f"разработчик злой {ex}")
        print("сделай нормально")
        continue
    finally:
        print('ура сработало') #выполняется после трай или эксепшена всегда выполняется в конце используют редко
    ab_sum = a+b
    print(f'Sum of {a} + {b} = {ab_sum}')
    print(f'{a} / {b} = {devision_score} ')
    print()