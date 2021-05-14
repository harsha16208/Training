import math
class Solution:
    def countPrimes(self, n: int) -> int:
        prime=['','']
        for i in range(2,n+1):
            prime.append(True)
        for j in range(2,int(math.sqrt(len(prime)-1))+1):
            if prime[j]==True:
                for k in range((j*j),len(prime),j):
                    prime[k]=False
        length=0
        for i in range(2,len(prime)):
            if prime[i]==True:
                length+=1
        return length
