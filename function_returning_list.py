# Function returning the list 
def show_list(li):
    print(li)
    print(type(li))
    for i in li:
        print(i)
    return li
list = [1,2,3,4,"Avinash"]
new_list = show_list(list)
print(new_list)
print(type(new_list))