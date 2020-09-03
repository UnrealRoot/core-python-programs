# Accessing elements in the array 
from numpy import*
'''
print("--------------------- Without using range() function --------------------- ")
stu_roll = array([1,2,3,4,5,6,7,8])
for elements in stu_roll:
     print(elements)     
#-------------------------------------------------------------------------------------------------
'''
print("--------------------- Using range() function { using index number }--------------------- ")
stu_roll = array([1,2,3,4,5,6,7,8])
n = len(stu_roll)
'''
stu_roll[3] = 1234 # Changing the element in position number 3
for i in range(n):
    print("Index ",i," = ",stu_roll[i])
    '''
#-------------------------------------------------------------
print("Using while loop")
i = 0
while i<n:
    print("Index ",i," = ",stu_roll[i])
    i+=1