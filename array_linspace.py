from numpy import*
# linspace divides elements in the array in (Last number denoted ) equal parts (HERE: 5)
a = linspace(1,8,5)
n =  len(a)
for i in range(n):
    print(a[i])
    
'''
------------- OUTPUT ------------- 
 1.0
2.75
4.5
6.25
8.0
    '''