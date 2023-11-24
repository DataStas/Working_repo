def sum_poly(a,b):
    na=len(a)
    nb=len(b)
    r=[]
    ia, ib=-1,-1
    while abs(ia)<=na or abs(ib)<=nb:
        c=0
        if abs(ia)<=na:
            c+=a[ia]
        if abs(ib)<=nb:
            c+=b[ib]
        r=[c]+r 
        ia-=1
        ib-=1
    i=0
    while r[i] ==0 and i<len(r)-1:
        i+=1
    return r[i:]  
    
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
r=sum_poly(a,b)
print(len(r)-1)
print(*r)