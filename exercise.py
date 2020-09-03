#number1 = input("Enter the first number")
#number2 = input("Enter the second number")
#number3 = input("Enter the third number")
#print(f"Average of entered numbers is : {(int(number1)+int(number2)+int(number3))/3}")

# Another way
print("................. Another way .................")
number1,number2,number3 = input("Enter three numbers seperated by commas ").split(",")
print(f"Average of entered numbers is : {(int(number1)+int(number2)+int(number3))/3}")
