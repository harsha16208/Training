def maxSubarrayXOR(N, arr):
    sum=[]
    for i in range(N):
      val=0
      for j in range(i,N):
          val^=arr[j]
      sum.append(val)
    print(max(sum))
maxSubarrayXOR(4,{1,2,3,4})
