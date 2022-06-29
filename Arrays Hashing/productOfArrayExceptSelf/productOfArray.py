# O(n) time complexity
# O(n) space complexity for prefix and postfix arrays

def productExceptSelf(nums):
    prefix=[1]
    postfix=[]
    pre=1
    pos=1
    res=[]
    for i in nums:
        pre*=i
        prefix.append(pre)
    for i in nums[::-1]:
        pos*=i
        postfix.append(pos)

    postfix=postfix[::-1]
    postfix.append(1)
    postfix.append(1)

    for i in range(1,len(nums)+1):
        res.append(prefix[i-1]*postfix[i])
    return res

# O(n) time complexity
# O(1) space complexity

def productExceptSelf(nums):
    res=[1] * len(nums)
        
    prefix=1    
    for i in range(len(nums)):
        res[i]=prefix
        prefix*=nums[i]   

    postfix=1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=postfix
        postfix*=nums[i]  
                
    return res
