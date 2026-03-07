n,k=map(int,input().split())
l=list(map(int,input().split()))
cur_sum=sum(l[0:k])
mini=0
min_sum=cur_sum
for i in range(1,n-k+1):
    cur_sum=cur_sum-l[i-1]+l[i+k-1]
    if(cur_sum<min_sum):
        min_sum=cur_sum
        mini=i
print(mini+1)
