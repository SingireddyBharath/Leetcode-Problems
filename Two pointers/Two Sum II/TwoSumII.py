# O(n) for worst case time complexity
# Using two poiters technique

def twoSum(numbers, target):
        
        l,r=0,len(numbers)-1        
        currSum=0
        currSum=numbers[l]+numbers[r]
        
        while l<r:
            currSum=numbers[l]+numbers[r]      
            if currSum>target:
                currSum=0
                r-=1
            elif currSum<target:
                currSum=0
                l+=1
            elif currSum==target:
                return [l+1,r+1]