class Solution:
    def convertEvenBitToZero (ob, n):
        temp=n
        bits=0
        sub=0
        while temp:
            if temp&1:
                sub+=1*2**bits
            bits+=2
            temp=int(temp/4)
        return n-sub
