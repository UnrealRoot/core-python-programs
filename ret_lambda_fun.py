# returning the lambda function 
def add():
    x = 10
    return(lambda y : x+y)
a = add()
print(a(20))