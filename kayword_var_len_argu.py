# keywoed variable length arguments
def add(**num):
    sum = num['a']  + num['b'] + num['c']
    print(sum)
add(a = 10,b = 20 , c = 30)