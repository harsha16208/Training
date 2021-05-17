class Solution:
	def setKthBit(self, N, K):
	    return N | 2**K
