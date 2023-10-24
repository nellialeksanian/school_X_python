a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]

# def mask_list (array: list[int], mask: list[int]) -> list [int]:
#     return [val*mask[i] for i, val in enumerate(array)]
# def test_mask_list():
#     print('проверяем тест на маск лист')
#     assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0]

# answer = mask_list(array = a , mask = b)
# test_mask_list()
# #print(answer)

# answer1 = [val*b[i] for i, val in enumerate(a)] #значене вал а умножили на значение б
# print(answer1)


# for i, val in enumerate(a):
#     print(f"index = {i}")
#     print(f'value = {val}')

matrix = [[1,3],[3,4],[1,4],[4,6]]
# print(matrix[0][0], matrix[1][0])

f1= [[0 for i in range(1)] for j in range(0,4)]
# print (f1)
i=0
# while i<4:
#     f1[i][0] = matrix[i][0]
#     i+=1
# print(f1)
# v2.matrix - (v2.matrix*f1.matrix / f1.matrix*f1.matrix) *f1.matrix


#  v1 = Matrix([[0],[0],[0],[0]])
#       v2 = Matrix([[0],[0],[0],[0]])
#       v3 = Matrix([[0],[0],[0],[0]])
#       v4 = Matrix([[0],[0],[0],[0]])
#       for i in range(v1.rows):
#          for j in range(v1.cols):
#             v1.matrix[i][j] = self.matrix[i][0]
#             v2.matrix[i][j] = self.matrix[i][1]
#             v3.matrix[i][j] = self.matrix[i][2]
#             v4.matrix[i][j] = self.matrix[i][3]
#       # try:
#          f1 = v1
#          f2 = v2-f1*(v2@f1)/(f1@f1)
#          f3 = v3-f1*(v3@f1)/(f1@f1)-f2*(v3@f2)/(f2@f2)
#          f4 = v4-f1*(v4@f1)/(f1@f1)-f2*(v4@f2)/(f2@f2)-f3*(v4@f3)/(f3@f3)
#       # except ZeroDivisionError:
         
      
#       return f1,f2,f3,f4

a=23.0
b=23.0
c=a/b
print(c)