a,b=map(int,input().split())
l=sorted(list(map(int,input().split())))
count=0
for i in range(a):
    if(l[i]+b<=5):
        count=count+1
print(count//3)
