list = []
n = int(input("Enter the number of elements : "))
for ele in range(n):
    list.append(input("Enter the element : "))
print("List : ")
for ele in range(n):
    print(f"{ele}. ",list[ele])