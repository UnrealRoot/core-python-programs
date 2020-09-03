# Passing array to the function
from array import*
def show_array(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)
a = array('i',[1,2,4,5,6,7])
show_array(a)