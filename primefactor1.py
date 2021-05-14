for i in range(int(input())):
    primes=['','']
    num=int(input())
    for j in range(2,num+1):
        primes.append(True)
    for k in range(2,len(primes)):
        if primes[k]==True:
            for l in range(k,len(primes),k):
                primes[l]=k
    prime_factors=set()
    while num>1:
        prime_factors.add(primes[num])
        num=int(num/primes[num])
    print(max(prime_factors))