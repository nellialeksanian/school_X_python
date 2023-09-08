from module import guess #импортируем функцию из соседнего файла
x=42
def outer ():
    y=12 #y не существует если мы не вызываем в функцию

    def answer(): #не можем на прямую вызвать так как находится фнутри функции
        return x
    return answer()


# n = int(input('enter number'))
# print(guess(n))

if __name__ == '__main__':
    x=42
    print(f'y in main exists {"y" in locals()}')
print(
    'y' in locals()  #locals те переменные которые мы сейчас можем достать,global для всех переменных (проверяем что у не существует
)
