# def my_personal_sum1(x: int or float, y: int or float) -> int or float:  # ->int это то что мы дадим
#     answer = x / y
#     return answer

def my_personal_sum2(numlist: list):
    answer = 0
    for num in numlist:
         answer += num
    return answer

_list = [1,2,3]
print(my_personal_sum2(_list))
