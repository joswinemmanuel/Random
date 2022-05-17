def star(n):
    mid=n*3
    num=n*4
    x=[]
    for i in range(1,num+1):
        i=' '*(num-i)+'* '*i
        x.append(i)
        
    emp=[]
    for i in x:
        if i.count('*')==mid:
            emp.append(i)
            break
        else:
            emp.append(i)
            
    for i in x[::-1]:
        if i.count('*')<mid:
            emp.append(i)
            
    for i in range(1,n+1):
        emp[(mid-1)-i]=x[len(x)-n]
        emp[(mid-1)+i]=x[len(x)-n]
        n-=1

    for i in emp:
        print(i)


def par(n):
    for i in range(1,n+1):
        print(' '*i+'* '*n)

def cir(n):
    mid=5+((n-1)*2)
    x=[]
    j=3+((n-1)*2)
    for i in range(1,n+2):
        x.append(' '*j+'* '*(2*i))
        j-=2
    emp=[]
    for i in x:
        emp.append(i)
    emp.append('* '*mid)
    for i in x[::-1]:
        emp.append(i)
    for i in emp:
        print(i)
cir(5)
print()
par(10)
print()
star(3)
    















        



    
        

            
