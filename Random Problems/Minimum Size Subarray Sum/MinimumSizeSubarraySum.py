# sliding window technique
# O(n) time complexity and O(1) space complexity

def minSubArrayLen(target,nums) -> int:
        l,currsum=0,0   # left pointer and Current sum
        ans=float("inf") # maximum value 
        
        for r in range(len(nums)):            
            currsum+=nums[r]            
            while currsum>=target:
                ans=min(ans,r-l+1)
                currsum-=nums[l]
                l+=1      
        
        if ans==float("inf"):
            return 0
        return ans
            