for i in range(int(input())):
    num=int(input())
    primes=['','']
    for j in range(2,num+1):
        primes.append(True)
    for k in range(2,len(primes)):
        if primes[k]==True:
            for l in range(k,len(primes),k):
                primes[l]=k
    output=''
    divisors=[]
    prime_factors=set()
    while num>1:
        divisors.append(primes[num])
        prime_factors.add(primes[num])
        num=int(num/primes[num])
    prime_factors=sorted(prime_factors)
    if 2 not in prime_factors:
        output+="2^0*"
    for m in prime_factors:
        output+="{0}^{1}*".format(m,divisors.count(m))
    print(output[0:len(output)-1])