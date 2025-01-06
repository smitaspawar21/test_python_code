import numpy as np

matrix1 = np.array([[
    [1,2,3],
    [4,5,6],
   
    ]])

matrix2 = np.array([[
    [10,11,12],
    [13,14,15]
    
]])

#output = matrix1 + matrix2

#print(output)

#output = matrix1 - matrix2

#print(output)

#print(matrix1.shape)

#row,column,dim = matrix1.shape

#print(matrix1)

#print(row)

#print(column)

new_matrix1 = np.array([1,2,3,4,5])

new_matrix2 = np.array([
                       [10,11,12,13,14],
                       [20,21,22,23,24]
                       ])

new_matrix3 = np.array([[[26,27,28,29,30],
                         [31,32,33,34,35],
                         [36,37,38,39,40]
                         ]])

#print(new_matrix1)

#print(new_matrix2)

#print(new_matrix3)

result1 = new_matrix1 +  new_matrix2

#print(result1)

#row2, col2, dim2 = new_matrix2.shape
#print(row2)

result2 = new_matrix1 +  new_matrix3

#print(result2)

#result3 = new_matrix2 +  new_matrix3

#print(result3)


result4 = new_matrix1 * new_matrix3

print(result4)



