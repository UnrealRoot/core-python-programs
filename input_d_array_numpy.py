# Taking the input in 2D array using numpy
from numpy import *
'''
r = int(input("Enter the numbers of rows :" ))
c= int(input("Enter the numbers of columns :" ))
arr_zero = zeros((r,c))
le = len(arr_zero)
print(arr_zero)
# Code for taking elements in the array
for i in range(r):
    for j in range(len(arr_zero[i])):
        x = int(input(f"Enter element of {r} rows and {c} columns  : "))
        arr_zero[i][j] = x
# For displaying elements in the array
for i in range(r):
    for j in range(len(arr_zero[i])):
        print(arr_zero[i][j])
'''
# Using while loop
row = int(input("Enter number of rows : "))
column = int(input("Enter number of columns : "))
arr = zeros((row ,column))
print(arr)
l = len(arr)
i = 0 
while i<l:
    j = 0
    while j<len(arr[i]):
        x = int(input("Enter the element : "))
        arr[i][j] = x
        j+=1
    i+=1 
    
i = 0
while i <l:
    j = 0 
    while j<len(arr[i]):
        print("elements are : ",arr[i][j])
        j+=1
    i+=1
print(arr)