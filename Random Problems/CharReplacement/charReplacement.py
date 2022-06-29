
# O(26*n) time complexity
# Dictionary and sliding window technique

def characterReplacement(s: str, k: int):        
        res=0
        count={}  # Dictionary for character count
        l=0
        for r in range(len(s)):
            #updating count for character
            count[s[r]]=1+count.get(s[r],0) 
            
            if (r-l+1)-max(count.values())>k: 
                count[s[l]]-=1
                l+=1

            # Maximum window length
            res=max(res,r-l+1) 

        return res

# Driver code
if __name__ == "__main__":
    input_str=input()
    k=int(input()) #maximum replacements
    print(characterReplacement(input_str,k))