name,char = input("Enter your name  & Enter any one character in your name( comma seperated ): ").split(",")
print(f"Length  of your name is {len(name)}")
print(f"Character count of your name is {name.lower().count(char.lower())}") # For case Insensitive character


