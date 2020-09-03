list = [1,1,3,-4,5.98,"Avinash"]
print("Before appending the new element in the list : ")
for ele in list:
    print(ele)
print("After appending the new element in the list : ")
list.append(990.8754)
for ele in list:
    print(ele)
# remove  method in list (It removes the first occurence )
list.remove(-4)
for ele in list:
    print(ele)
# index() method (It returns the index of the first occurence of the element)
ele_index = list.index(5.98)
print("Index is : ",ele_index)
# reverce() method (It reverce the elements in the list )
list.reverse()
for ele in list:
    print(ele)

# count() method 
list_new = [1,2,1,3,9,5]
c = list_new.count(1)
print("Count is : ",c) 
# sort() methos sorts the elements in acsending order (not string and char )
list_new.sort()
print("After sortind : ",list_new)

# clear() method 
list_new.clear()
print("After clearing : ",list_new)
