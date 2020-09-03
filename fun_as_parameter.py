# Passing a function as a parameter 
def disp(sh):
    print("disp function" + sh())
def show():
    return " show function"
disp(show)