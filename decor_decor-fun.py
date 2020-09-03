# decorating the functon two times 
def decor1(num):
    def inner():
        a = num()
        multi = a*5
        return multi
    return inner

def decor2(num):
    def inner():
        b = num()
        add = b+5
        return add
    return inner
# @decor1
# @decor2

def num():
    return 10

num = decor2(decor1(num))  # If you dont want to write this go to line number 15,16
print(num())