def prefixCalculator(a):
    prefix=[]
    for j in range(n):
        if j==0:
            prefix.insert(0,a[0])
        else:
            prefix.insert(j,prefix[j-1]+a[j])
    return prefix
for i in range(int(input())):
    n=int(input())
    a=[]
    a.extend([int(x) for x in input().split(' ')])
    prefix=prefixCalculator(a)
    for area in range(len(a)):
        if not a[area]==-1:
            print(a[area],end=' ')
        else:
            a[area]=int((prefix[area-1]/(area)))
            prefix=prefixCalculator(a)
            print(a[area],end=' ')
    print()
