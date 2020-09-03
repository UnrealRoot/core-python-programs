x = [1,2,3,4,5,6,7,8]
print("Original list: ")
n = len(x)
for i in range(n):
    print(i," = ",x[i])
print()
print("From 1st position to 4th position: ")
a = x[1:5]
for i in a:
    print(i)
print()

print("From 0 position to last position: ")
a = x[0:]
for i in a:
    print(i)
print()

print("From 0 position to 4th position: ")
a = x[:5]
for i in a:
    print(i)
print()

print("Last 4 Elements: ")
a = x[-4:]
for i in a:
    print(i)
print()

print("From 0 position to 6th position with step 2 : ")
a = x[0:7:2]
for i in a:
    print(i)
print()

print("Last 5 Elements with [-5-(-3)] = 2 Elements towards right: ")
a = x[-5:-3]
for i in a:
    print(i)
print()