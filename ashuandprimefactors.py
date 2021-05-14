for i in range(int(input())):
    def sieve(num):
        primes=['','']
        for l in range(2,1000001):
            primes.append(True)
        for j in range(2,len(primes)):
            if primes[j]==True:
                for k in range(j,len(primes),j):
                    if primes[k]==True:
                        primes[k]=j
        print(primes.count(num))
    sieve(int(input())
