a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]

def mask_list (array: list[int], mask: list[int]) -> list [int]:
    return [val*mask[i] for i, val in enumerate(array)]
def test_mask_list():
    print('проверяем тест на маск лист')
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0]

answer = mask_list(array = a , mask = b)
test_mask_list()
print(answer)

# answer1 = [val*b[i] for i, val in enumerate(a)] #значене вал а умножили на значение б
# print(answer1)


# for i, val in enumerate(a):
#     print(f"index = {i}")
#     print(f'value = {val}')