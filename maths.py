import numpy as np

arr1 = np.array([10,11,12,13,14])
arr2 = np.array([20,21,22,23,24])

mul = arr1 * arr2

add = arr1 + arr2

sub = arr2 - arr1

div = arr2 / arr1

print("MULtiplication :",mul)

print("Addition :",add)

print("Subtraction :",sub)

print("Division :",div)


complex_cal = (arr1 * arr2 ) / (arr1 + arr2) - (arr1 / arr2)

print(" complex :",complex_cal)
