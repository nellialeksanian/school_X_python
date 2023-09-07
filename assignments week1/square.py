n = int(input("Введите число"))
array: list = []
for num in range(-n,n+1):
    array.append(num**2)
print(array)