class Solution:
    def setBits(self, N):
        count=0
        while N>0:
            if N & 1 >0:
                count+=1
            N>>=1
        return count
