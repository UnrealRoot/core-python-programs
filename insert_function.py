# insert function
from array import *
st = array('i',[1,2,3,4,5,6,7,8,9,10])
n = len(st)
print("Length of the array is : ",n)
i=0
while i<n:
    print(st[i])
    i+=1
print("---------------------------- after insert() ----------------------------- ")
st.insert(10,12345)
st.insert(2,4567)
n = len(st)
j = 0
while j<n:
    print(st[j])
    j+=1