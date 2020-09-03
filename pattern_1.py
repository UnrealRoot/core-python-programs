'''for i in range[4:3:1]:
   # for j in range[4:i:-1]:
        print(" * ")
 #   print("  ")
 '''
 
#rows = 5
#num = rows
for i in range(5, 0, -1):
    for j in range(0, i):
        print(" * ", end=' ')
    print("\r")