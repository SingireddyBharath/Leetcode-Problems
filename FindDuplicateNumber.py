class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast=0,0
        
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                break
        slow2=0
        
        while True:
            if slow2==slow: return slow
            slow2=nums[slow2]
            slow=nums[slow]
