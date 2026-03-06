n,m=map(int, input().split())
l=sorted(list(map(int, input().split())))
k=[]
for i in range(len(l)-(n-1)):
    d=l[i+(n-1)]-l[i]
    k.append(d)
print(min(k))
