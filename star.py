import numpy as np

#for i in range(5):
 
    #for j in range(1,6):
        
       
       # print("*",end = "\t")
    
    #print("")
    

arr_3x3 = []

count = 1
for k in range(1,4):
    dim = []
    for i in range(1,4):
        row = []

        for j in range(1,4):
            row.append(count)
            count *= i
       
        arr_3x3.append(row)
    dim.append(arr_3x3)

#print(dim)
#print(arr_3x3)
print(dim[0][4][0])
#for dim in arr_3x3:
#for row in dim:
        #print(row)        