# decoration function 
def decor(num):
    def inner():
        a = num()
        add = a+5
        return add
    return inner

def num():
    return 10

num = decor(num)
print(num())