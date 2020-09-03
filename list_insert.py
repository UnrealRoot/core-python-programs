# Insert() method in list 
list = [1,2,3,4,5,"Avinash "]
list.insert(6,"Mankar")
for ele in list:
    print(ele)
# pop() method in list 
list.pop()
for ele in list:
    print(ele)
# pop(n) method in list 
n = list.pop(2)
for ele in list:
    print(ele)
print("Removed element : ",n)