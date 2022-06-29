# Using Set 
# O(n) time complexity 

def longestConsecutive(nums) -> int:
        numSet=set(nums)
        res=0        
        for n in nums:
            # check if it is start of sequence
            if (n-1) not in numSet:
                length=0                
                while (n+length) in numSet:
                    length+=1                    
                res=max(res,length)
                
        return res