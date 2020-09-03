import sys
print(sys.getrecursionlimit())
# To change the limit of the recursion 
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def myfun():
    global i
    i+=1
    print(f"{i}. Recursion ")
    myfun()
myfun()