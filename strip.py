# Program to implement strip method 
# lstrip() Method is used to delete left-side-space in the string
# rstrip() Method is used to delete right-side-space in the string
# strip() Method is used to delete Both-side-space in the string
name = "   Avinash   "
dots = "..."
print(name + dots)
print("To print the string without spaces ")
print( name.lstrip() + dots )
print( name.rstrip() + dots )
print( name.strip() + dots )