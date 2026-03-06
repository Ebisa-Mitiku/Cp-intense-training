n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
d=l[0:k]
t=l[k:]
if(k==0):
    if(l[0]>1):
        print(1)
    else:
        print(-1)
elif(n==1 and k==1):
    print(l[0])
elif(k==n):
    print(l[n-1])
elif(max(d) in t):
    print(-1)
else:
    print(max(d))

 
