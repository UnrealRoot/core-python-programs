# These all are the string functions 
name = "  Avinash   "
dig = "1234"
spa = "  "
print(name.upper())    # Converts the string into upper case
print(name.lower())    # Converts the string into lower case
print(name.swapcase()) # Converts the string upper to lower and lower to upper
print(name.title())    # Converts the strings first letter  into upper case and others in lower case
print(name.isupper())  # Check weather string is upper or not 
print(name.islower())  # Check weather string is lower or not
print(dig.isdigit())   # Check weather string has all digits  or not
print(dig.isalpha())   # Check weather string has all alphabets  or not
print(dig.isalnum())   # Check weather string is all alpha-numeric or not
print(spa.isspace())   # Check weather string has spaces or not
print(name.lstrip())   # Removes the spaces from left of the string 
print(name.rstrip())   # Removes the spaces from right of the string
print(name.replace("Avi","AVINA")) 
name1 = "Hello-How-are-you"
print(name1.split("-"))
print("-".join(name1))
print(name1.startswith("A"))
print(name1.endswith("H"))


'''

----------------- OUTPUT  ---------------------
$ python strinr_function.py
AVINASH
avinash
aVINaSH
Avinash
False
False
True
False
True
'''