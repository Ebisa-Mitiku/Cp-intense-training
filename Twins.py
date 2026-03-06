n=int(input())
l=sorted(list(map(int,input().split())))
coin=sum(l)/2
l.reverse()
x=0
c=0
for i in range(n):
    x=x+l[i]
    c=c+1
    if(x>coin):
        break  
print(c)
