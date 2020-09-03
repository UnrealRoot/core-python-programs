def Hello(pc):
    def Wel():
        return "Hello, "
    res = Wel() + "Welcome "+ pc
    return res
a = Hello("To my PC")
print(a)