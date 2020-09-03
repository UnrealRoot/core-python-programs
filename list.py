a = [10,20,-50,30.44,"Avinash"]
# Accessing with +ve index
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# Accesing with -ve index
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print("Before modifying the list")
print(a) 
# modifying the elements in the list      
a[1]=12345
print("After modifying the list")
print(a)  # After midifying the list Address does not changes (because it is mutable) 