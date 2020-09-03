# Ananomous function or Lambda function
# Syntax:
#  lambda argument_list : expression
show = lambda x  : print(x)
show(4)
#--------------------------------------------
add = lambda x,y : x+y
print(add(5,10))
#--------------------------------------------
add_sub = lambda x,y : (x+y,x-y)
a, s = add_sub(20,10)
print(a,s)
#--------------------------------------------
addition = lambda x,y = 10 : x+y
print(addition(20))
#--------------------------------------------
