# Higher order function in the list 
a = [10,20,30,40,50,60,5,-4,23,65]
def high_element(n):
    if n>=60:
        return True
result = list(filter(high_element,a))
print(type(result))
for i in result :
    print(i)
# Above code using lamda function 
a = [10,20,30,40,50,60,5,-4,23,65]
result = list(filter(lambda n:(n>=60),a))     #If we write None insted of (n>=60) it will only returns the true elements
print(type(result))
for i in result :
    print(i)