class Solution:
    def nextGreaterElement(self,nums1, nums2):
        ans=[-1]*len(nums1)     
        for i in nums1:
            temp=nums2.index(i)
            for j in range(temp,len(nums2)):
                ans[nums1.index(i)]=-1
                if nums2[j]>i:
                    ans[nums1.index(i)]=nums2[j]
                    break   
        return ans