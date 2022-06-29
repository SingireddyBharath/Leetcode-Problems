# Brute force approach
# O(n^2) time complexity because checking for all possible combinations

def maxArea(height) -> int:
    res=0

    for L in range(len(height)):
        for r in range(len(height)):
            area=(r-L)*min(height[L],height[r])
            res=max(res,area)

    return res



# optimal approach
# Two pointer approach
# O(n) time complexity

def maxArea(height) -> int:
        
        l,r=0,len(height)-1    
        res=0        
        while l<r:            
            minheight=min(height[l],height[r])
            area=(r-l)*minheight         
            res=max(res,area)
            if height[l]==minheight:
                l+=1
            else:
                r-=1
                
        return res