# Brute Force approach
# O(n^2) time complexity


def maxProfit(prices) -> int:
    res=0
    for i in range(len(prices)) :
        for j in range(len(prices)):
            res=max(res,prices[j]-prices[i])
    return res


# Two pointers technique
# O(n) time complexity

def maxProfit(prices) -> int:
        l,r=0,1
        res=0        
        while r<len(prices):           
            
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                res=max(res,profit)                
            else:
                l=r
            r+=1
            
        return res