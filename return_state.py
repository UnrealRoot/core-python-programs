def add():
    x = 10
    y = 20
    c = x+y
    return c
sum = add()  # This is because... return statement give returned value in the statement give it to add() statement
print(sum)
#----------------------------------------------------------------
def add_sub(y):
    x = int(input("Enter the value : "))
    c = x+y
    d = x-y
    return(c,d)
sum,sub = add_sub(20)
print(sum)
print(sub)