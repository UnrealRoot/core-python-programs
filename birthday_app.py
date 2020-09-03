# This is the birthday reminder program 
dict = {}
while True:
    print("------------------- Birthday app ------------------- ")
    print("1. show Birthday ")
    print("2. Add to Birthday list ")
    print("3. Exit ")
    choice = int(input("Enter your choice from above : "))
    if (choice == 1):
        if (len(dict.keys()) == 0):
            print("Till no Birthdays are added to your list\n ")
        else: 
            name = input("Enter the name to look for the Birthday \n")
            Birthday = dict.get(name,"No Birthday to show ")
            print(Birthday)
    elif choice == 2:
        name = input("Enter Friend's Name ")
        date = input("Enter Birthdate ")
        dict[name] = date
        print("Bitrhday addes sucessfully ")
    elif choice == 3:
        break
    else:
        print(" Please Choose the valid option  ")