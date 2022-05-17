nm = input().split()
n = int(nm[0])
m = int(nm[1])
l=[0]*(n+1)
for _ in range(m):
    a,b,k=map(int, input().rstrip().split())
    for j in range(a,b+1):
            l[j]+=k
m=max(l[1:])
print(m)
    
    

