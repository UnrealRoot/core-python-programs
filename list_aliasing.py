# Aliasing list
a = [10,20,30,40,50]
b = a
print("A: ",a)
print("B: ",b)
print()
print("Modifying A: ")
a[2] = 55
print("A: ",a)
print("B: ",b)
print()
print("Modifying B: ")
b[3] = 123
print("A: ",a)
print("B: ",b)

