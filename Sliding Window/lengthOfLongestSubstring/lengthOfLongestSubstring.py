# Using Sliding Window technique
# O(n) time complexity  

def lengthOfLongestSubstring(s) -> int:
        cha=set()        
        l,r=0,0
        res=0
        while r<len(s):            
            while s[r] in cha:
                cha.remove(s[l])
                l+=1                
            cha.add(s[r])            
            res=max(res,len(cha))
            r+=1
        return res