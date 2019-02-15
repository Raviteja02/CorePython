
#NonDefault Parameters: we will pass values to the non default parameters at the time of calling the function.
def add(a,b):
    c = a+b
    print(c)

add(100,200)
add(200,300)
print(add) #function address storing in a variable with the name of the function.
sum=add    #we can assign the function variable to any user defined variable.
sum(10,20) #and we can access the function with that variable name.


#Default Parameters: we will pass values to the default parameters while creating the function.

def sub(d=20,e=30):
    f=e-d
    print(f)
sub()
sub(30)
sub(10,40) #if we pass values to default parameters it will override the existing values and give results.

def mult(g,h=10):   #one NonDefault and Default Parameter.
    i=g*h
    print(i)
mult(20)

#def div(j=10,k):   #error Default parameter folows Nondefault parameter.
#    l=j/k          #it wont work.,we can't define a Nondefault parameter after defining Default parameter.

#Orbitary Parameters: the parameters which are preceeded by the (*) are konwn as orbitary Parameters.

def ravi(*a):       #Single Star Orbitary Parameter it returns tuple as a result.
    print(a)
    print(type(a))
ravi()
ravi(10,20,30)

def teja(j,*k):
    print(j)
    print(type(j))
    print(k)
    print(type(k))
teja(10,20,30,40)


#def sai(*l,m): Nondefault parameter follwed by sigle star 0rbitary parameter will wont work
#    print(l)
#    print(type(l))
#    print(m)
#    print(type(m))

#sai(5,60,70,80)


def satya(*l,m):     #Nondefault parameter follwed by sigle star 0rbitary parameter will wont work
    print(l)
    print(type(l))
    print(m)
    print(type(m))

satya(5,60,70,80,m=90)

def sai(*l,m=20):
    print(l)
    print(type(l))
    print(m)
    print(type(m))

sai(8,40,70,60)

def myfunc(**a):     #Multi Star Orbitary Parameter and it will return dictionary as a result
    print(a)
    print(type(a))
myfunc(x=10,y=20,z=30)

#Arguments

#NonKeyWord Arguments  also known as positional arguments.

def nonkeyword(name,msg):
    print("Hello",name,msg)
nonkeyword("raviteja","good Morning")

nonkeyword("good Morning","Raviteja")


#Keyword Arguments also known as NOnPositional Arguments.


def keyword(name,msg):
    print("Hello",name,msg)
keyword(name="raviteja",msg="good Morning")
keyword(msg="good Morning",name="raviteja")
