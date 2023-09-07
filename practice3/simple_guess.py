
def guess(num: int) -> int or str:
    for i in range(1, num+1):
        if num/i == i:
            return i
    return 'трудно'

x = int(input('enter number'))
print(guess(x))

