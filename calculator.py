# Program for scientific calculator
print("Your choices ....!!")
print("1. addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")
print("6. LCM")
print("7. HCM")
print("8.Convert USD into INR")
print("9.Convert INR into USD ")
print("10.How much old you are ..??")

choice = int(input(print("Please Enter your choice : ")))
if(choice == 1):
    num1 = int(input(print("Enter the first number :")))
    num2 = int(input(print("Enter the second number :")))
    print(f"You have entered \'{num1}\' and \'{num2}\' ")
    add = num1+num2
    print(f"Addition of {num1} and {num2} is :  ",add)
elif(choice == 2):
            num1 = int(input(print("Enter the first number :")))
            num2 = int(input(print("Enter the second number :")))
            print(f"You have entered {num1} and {num2} ")
            sub = num1-num2
            print(f"Addition of {num1} and {num2} is :  ",sub)
elif (choice == 3):
            num1 = int(input(print("Enter the first number :")))
            num2 = int(input(print("Enter the second number :")))
            print(f"You have entered {num1} and {num2} ")
            mul = num1 * num2
            print(f"Addition of {num1} and {num2} is :  ", mul)
elif (choice == 4):
            num1 = int(input(print("Enter the first number :")))
            num2 = int(input(print("Enter the second number :")))
            print(f"You have entered {num1} and {num2} ")
            div = num1 / num2
            print(f"Addition of {num1} and {num2} is :  ",div)
elif (choice == 5):
            num1 = int(input(print("Enter the first number :")))
            num2 = int(input(print("Enter the second number :")))
            print(f"You have entered {num1} and {num2} ")
            avg = (num1+num2)/2
            print(f"Average of {num1} and {num2} is : ",avg)
elif (choice == 6):
            num1 = int(input(print("Enter the first number :")))
            num2 = int(input(print("Enter the second number :")))
            print(f"You have entered {num1} and {num2} ")
            def compute_lcm(x, y):
                if x > y:
                    greater = x
                else:
                    greater = y

                while (True):
                    if ((greater % x == 0) and (greater % y == 0)):
                        lcm = greater
                        break
                    greater += 1

                return lcm
            print("The L.C.M. is", compute_lcm(num1, num2))
elif(choice==7):
    num1 = int(input(print("Enter the first number :")))
    num2 = int(input(print("Enter the second number :")))
    print(f"You have entered {num1} and {num2} ")
    def hcf(x, y):
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller + 1):
            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf
    print("The H.C.F. of", num1, "and", num2, "is", hcf(num1, num2))
elif(choice==8):
    USD = float(input("Please enter USD amount:"))
    INR = USD * 76.25
    print(INR, " Rupees      ..NOTE : This  may be change according to the forex market")
elif(choice==9):
    INR = float(input("Please enter INR amount:"))
    USD = (INR/76.25)
    print(USD, " $     ..NOTE : This  may be change according to the forex market")
elif(choice==10):
    Date  = int(input(print("Date  : ")))
    Month = int(input(print("Month : ")))
    Year  = int(input(print("Year  : ")))
    DOB   = Date + Month + Year
    In_years  = 2020 - Year
    In_months =(In_years*12*Month)
    In_days   =(In_years*In_months*365)
    print("In year   : ",In_years)
    print("In Months : ",In_months)
    print("In Days   : ",In_days)

else:
    print("Sorry...!!! you have entered wrong input")
