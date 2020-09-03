# Program to print the characters on the both sides of the Entered string
# syntax :
# center(string_size+nos.of characters ,"character")

#name = "Avinash"
#print(name.center(11,"*"))
name = input("Enter your name : ")
print(name.center(len(name)+8," * "))