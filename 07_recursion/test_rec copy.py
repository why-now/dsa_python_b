def a():
    b()
    print(5)
    
def b():
    c()
    print(4)
    
def c():
    d()
    print(3)

def d():
    e()
    print(2)

def e():
    print(1)

a() # start