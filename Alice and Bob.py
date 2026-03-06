n = int(input())
l = list(map(int, input().split()))
if n == 1:
    print(1, 0)
else:
    left = 0
    right = n - 1
    a = l[left]
    b = l[right]
    left += 1
    right -= 1
    ca = 1
    cb = 1
    while left <= right:
        if a < b:
            a += l[left]
            ca += 1
            left += 1
        elif b < a:
            b += l[right]
            cb += 1
            right -= 1 
        else:
            if left != right:
                a += l[left]
                ca += 1
                left += 1
                
                b += l[right]
                cb += 1
                right -= 1
            else:
                ca += 1
                break
    print(ca, cb)
