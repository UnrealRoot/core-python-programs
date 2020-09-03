# This is the example of nested lambda function
add = lambda x=10 : (lambda y : x+y) #-------
                                     #       |  This lambda finction is Raturned here 
                                     #       |
a = add()   #<<-------------------------------
print(a(5))       #          