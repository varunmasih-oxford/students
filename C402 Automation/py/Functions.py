# Python functions – define and reuse.
# Pre-defined (print(), int(), input() ) and user defined (add(), abc(), xyz() ) functions.


x = 10
y = 10
z = x+y

x = 10
y = 10
z = x+y

x = 10
y = 10
z = x+y

def abc():
    x = 10
    y = 10
    z = x+y
    print(z)

abc()
abc()
abc()

def add():
    x = 10
    y = 10
    z = x+y
    print(z)

add()
add()
add()

def add(x, y):
    z = x+y
    print(z)

add(10,20)
add(1000,2000)

def add(om, tm=500):
    per = om/tm*100
    print(per)


add(300)
add(300,300)


