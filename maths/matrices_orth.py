import math

class Matrix:

   def __init__(  
         self, 
         matrix = [],
         rows: int = 0,
         cols: int = 0,
      ):
         self.matrix = matrix
         self.rows = len(self.matrix)
         self.cols = len(self.matrix[0])
        

   def __matmul__(self, other): 
         result = 0
         for i in range(self.rows):
            for j in range(self.cols):
                  result += self.matrix[i][j] * other.matrix[i][j]
         return result

   def __sub__(self, other):  
      if isinstance(other, Matrix):
         if (self.rows, self.cols) != (other.rows, other.cols):
            raise ArithmeticError('Matrices are NOT the same size.')
         else: 
            new_matrix = []
            for i in range(self.rows): #строку
               temp_row = []
               for j in range(self.cols): #столбцы
                  temp_row.append(self.matrix[i][j]-other.matrix[i][j])
               new_matrix.append(temp_row)
            return Matrix(new_matrix)
      elif isinstance(other, int | float):
          new_matrix = []
          for i in range(self.rows): #строку
               temp_row = []
               for j in range(self.cols): #столбцы
                  temp_row.append(self.matrix[i][j] - other)
               new_matrix.append(temp_row)
          return Matrix(new_matrix)
      
   def __mul__(self, other): 
          new_matrix = []
          for i in range(self.rows): #строку
               temp_row = []
               for j in range(self.cols): #столбцы
                  temp_row.append(self.matrix[i][j] * other)
               new_matrix.append(temp_row)
          return Matrix(new_matrix)
      
   def is_zero_matrix(self, vector):
      return all(vector.matrix[i][j] == 0.0 for i in range(vector.rows) for j in range(vector.cols))  

   def vector_projection(self, v, f):
    if self.is_zero_matrix(f) == False:
      try:
         v_dot_f = v@f
         f_dot_f = f@f
         projection = f*(v_dot_f/f_dot_f)
         return projection
      except ZeroDivisionError as e:
         print(f'error {e}')
    else:
      return 0

   def normalize_vector(self, vector):
    magnitude = math.sqrt(vector@vector)
    result = []
    for i in range(vector.rows):
       for j in range(vector.cols):
         result.append(vector.matrix[i][j] / magnitude)
    return result
   
   def orthogonalization(self):
      v1 = Matrix([[0],[0],[0],[0]])
      v2 = Matrix([[0],[0],[0],[0]])
      v3 = Matrix([[0],[0],[0],[0]])
      v4 = Matrix([[0],[0],[0],[0]])
      for i in range(v1.rows):
         for j in range(v1.cols):
            v1.matrix[i][j] = self.matrix[i][0]
            v2.matrix[i][j] = self.matrix[i][1]
            v3.matrix[i][j] = self.matrix[i][2]
            v4.matrix[i][j] = self.matrix[i][3]

      f1 = v1
      f2 = v2-self.vector_projection(v2, f1)
      f3 = v3-self.vector_projection(v3, f1)-self.vector_projection(v3, f2)
      f4 = v4 - self.vector_projection(v4, f1) - self.vector_projection(v4, f2) - self.vector_projection(v4, f3)

      basis = [f1, f2, f3, f4]
      normalized_basis=[]

      for i in range(len(basis)):
         if self.is_zero_matrix(basis[i]) == False:
            normalized_basis.append(self.normalize_vector(basis[i]))
      
      return normalized_basis
   

   def __repr__(self):
      return str(self.matrix)  


if __name__ == "__main__":
   matrix1 = Matrix([
      [1,2,1,7],
      [1,2,0,1],
      [0,3,3,3],
      [3,4,9,9]
   ])
   print(matrix1.orthogonalization())
          