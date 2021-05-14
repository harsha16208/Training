from math import sqrt as s
for i in range(int(input())):
    l,r=[int(x) for x in input().split(" ")]
    def sumOfPrimes(l,r):
        primes=['','']
        for i in range(2,r+1):
            primes.append(True)
        for j in range(2,int(s(r))+1):
            if primes[j]==True:
                for k in range(j*j,r+1,j):
                    primes[k]=False
        sum=0
        for m in range(l,len(primes)):
            if primes[m]==True:
                sum+=m
        print(sum)
    sumOfPrimes(l,r)
