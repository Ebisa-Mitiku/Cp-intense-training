n=int(input())
l=list(map(int,input().split()))
dima=0
sera=0
for i in range(n-1):
    if((i+1)%2!=0):
        if(l[0]>=l[len(l)-1]):
            sera=sera+l[0]
            del l[0]
        else:
            sera=sera+l[len(l)-1]
            del l[len(l)-1]
    else:
        if(l[0]>=l[len(l)-1]):
            dima=dima+l[0]
            del l[0]
        else:
            dima=dima+l[len(l)-1]
            del l[len(l)-1] 
if(n%2==0):
    dima=dima+l[0]
else:
    sera=sera+l[0]
print(sera,dima)
