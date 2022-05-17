def a(n):
    for i in range(1,n+1):
            print(('*'*i))

def b(n):
    for i in range(1,n+1):
        print(('*'*i).rjust(n))

def c(n):
    for i in range(1,(n*2)+1,2):
        print(('*'*i).center(n*2))

def d(n):
    for i in range(n,0,-1):
        print(('*'*i))

def e(n):
    for i in range(n,0,-1):
        print(('*'*i).rjust(n))

def f(n):
    for i in range((n*2)-1,0,-2):
        print(('*'*i).center((n*2)-1))

def g(n):
    for i in range(1,n+1):
        print((n-i)*' ',(i*'* '))

def h(n):
    for i in range(n,0,-1):
        print((n-i)*' ',(i*'* '))

''' UNDERSTAND ALL FOR GOOD USE '''

a(6)
