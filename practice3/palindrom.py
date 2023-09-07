def palindrome(x: int):
    x = str(x)
    if x == x[len(x)::-1]:
        return 'палиндром'
    return 'не палиндром'

n = input('enter')
print(palindrome(n))
