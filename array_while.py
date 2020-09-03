from array import *
st = array('i',[1,2,3,4,5,6,7,8,9,10])
n = len(st)
print("Length of the array is : ",n)
i=0
while i<n:
    print(st[i])
    i+=1
print("--------------------------------------------------------")
print("After append")
st.append(11)
st.append(12)
st.append(13)
st.append(20)
n = len(st)
j = 0
while j<n:
    print(st[j])
    j+=1