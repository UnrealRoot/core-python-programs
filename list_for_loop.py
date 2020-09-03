# Accessing the elements of the list using for loop
list = [1,2,3,-4,5.6,'Avinash']
# Accessing the eements without index 
for elements in list:
    print(elements)
# Accessing the elements with index
n = len(list)
for ele in range(n):
    print(ele,list[ele])
