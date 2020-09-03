from numpy import*
n = int(input("Enter the number of elements : "))
a = zeros(n,dtype=int) # Here we created the array with elements  ZERO (int) values
for i in range(len(a)):
    x = int(input("Enter the element : "))
    a[i] = x
    
print("Entered elemets in the array are : ",a)
               