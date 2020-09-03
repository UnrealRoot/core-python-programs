# Program to take more than one input at a time 
name , age = input("Enter your name and age ").split()
# Here .split function is used to take input including some space
print(name)
print(age)
# Other way to take input saperated by commma 
name , age = input("Enter your name and age (Sepereted by comma) ").split(",")
print(name)
print(age)