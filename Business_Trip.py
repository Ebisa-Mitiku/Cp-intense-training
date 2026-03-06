n=int(input())
l=sorted(list(map(int,input().split())))
l.reverse()
x=0
c=0
for i in range(12):
    x=x+l[i]
    c=c+1
    if(x>=n):
        break

if(n==0):
    print(0)
elif(x<n):
    print(-1)
else:
    print(c)
