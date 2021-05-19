class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Set<List<Integer>> result=new HashSet();
        permutations(nums,0,result);
        return new ArrayList(result);
            
    }
    
    void permutations(int nums[],int start,Set<List<Integer>> result)
    {
        if(start==nums.length){
            result.add(arrayToList(nums));
        }
        for(int i=start;i<nums.length;i++)
        {
            swap(nums,i,start);
            permutations(nums,start+1,result);
            swap(nums,i,start);
        }
        
    }
    
    void swap(int nums[],int i,int j)
    {
        int temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
    }
    
    List<Integer> arrayToList(int nums[])
    {
        List<Integer> list=new ArrayList();
        for(int i:nums){
            list.add(i);
        }
        return list;
    }
    }
