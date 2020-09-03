# In this program i have tried to create the smart calculator
def add():
    global temp
    temp=0
    for x in range(length):
         temp=temp+list[x]
    return(temp)

def mul():
  mu=1
  for x in range(len(list)):
       mu=mu*list[x]
  return(mu)
def sub():
    global x
    global y
    x,y=list
    return(x-y)
def division():
    x,y=list
    return(x/y)
def reminder():
    x,y=list
    return(x%y)
def SMALL():
    small=list[0]
    for x in range(1,length):
        if(small>list[x]):
            small=list[x]
    return(small)
def LARGE():
     large=list[0]
     for x in range(1,length):
         if(large<list[x]):
             large=list[x]
     return(large)
def HCF():
    for i in range(SMALL(),0,-1):
        for j in range(length):
            if(length-1==j):
                if(list[j]%i==0):
                    return(i)
                else:
                     break


            if(list[j]%i==0):
                pass
            else:
                break
def LCM():
    large=LARGE()
    for i in range(large,mul()+1,large):
        for j in range(length):
            if(length-1==j):
                if(i%list[j]==0):
                    return(i)
            if(i%list[j]==0):
                pass
            else:
                break

def FIBONACCI():
    previous=0
    next=1
    temp=0
    for i in range(list[0]):
        print(previous,end=' ')
        temp=previous;
        previous=next
        next=temp+previous
def FACTORIAL():
    fact=1
    for i in range(list[0],1,-1):
        fact=fact*i
    return(fact)  
       
    


print('Welcome to smart calculator')
print('My name is \'Champakali\'')
i=1
while(i):
   list=[]
   str1=input('enter some text:')
   for s in str1.split():
        if(s.isdigit()):
            list.append(eval(s))
   str2=str1.lower()
   length=len(list)

   if('end' in str2):
       print("\nOk.. See you soon..!!")
       i=0

   elif('name' in str2 and 'boss' not in str2):
       print('My name is \'Champakali \' ')
   elif('add' in str2 or 'plus' in str2):
        print('addition is =',add())
   elif('sub' in str2):
        print(sub())
   elif('mul' in str2):
        print('multiply is=',mul())
   elif('divi' in str2):
        print(division())
   elif('modu' in str2):
       print(reminder())

   elif('exp' in str2):
        for x in str1.split():
            if(x.isalpha()):
               pass
            else:
               print(eval(x))

   elif('hcf' in str2 or 'gcd' in str2):
          print('hcf is =',HCF())
   elif('lcm' in str2):
       print(LCM())
   elif('fibon' in str2):
       FIBONACCI()
       print('')
   elif('fact' in str2):
       print(list[0],'factorial is =',FACTORIAL());
   elif('boss' in str2):
       print('my boss name is Avinash Mankar')