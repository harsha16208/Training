import math
prime=['','']
for i in range(2,int(input())+1):
    prime.append(True)
for j in range(2,int(math.sqrt(len(prime)-1))+1):
    if(prime[j]==True):
        for k in range((j*j),len(prime),j):
            prime[k]=False
for i in range(2,len(prime)):
    if prime[i]==True:
        print(i,"  ",end='')
