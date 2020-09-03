list = ["Shahrukh khan","salman khan","Hritik roshan","Govinda","Sunny Deol","Jacky shroff"]
import random
a = random.randint(0,len(list))
name = input(" Please Enter your name : ")
print(name + " looks like "+list[a])