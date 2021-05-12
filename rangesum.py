for i in range(int(input())):
    a=[]
    prefix=[]
    n=int(input())
    a.extend([int(x) for x in input().split(' ')])
    for j in range(n):
        if j==0:
            prefix.insert(0,a[0])
        else:
            prefix.insert(j,prefix[j-1]+a[j])
    for k in range(int(input())):
        l,r=[int(x) for x in input().split(' ')]
        if l==1:
            print(prefix[r-1])
        else:
            print(prefix[r-1]-prefix[l-2])
