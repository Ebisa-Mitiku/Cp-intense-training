n=int(input())
for i in range(n):
    x=int(input())
    l=list(map(int,input().split()))
    final=[]
    for i in range(1,x+1):
        if(i%2!=0):
            final.append(l[0])
            del l[0]
        else:
            final.append(l[len(l)-1])
            del l[len(l)-1]
    print(*final)
