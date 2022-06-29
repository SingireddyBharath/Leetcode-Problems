# O(m*nlogn)  time complexity  
# where m is the number of strings in the input
# and nlogn is to sort every string

def groupAnagrams(strs):
        
        ana_count = {}
        for ele in strs:
			# converting it to tuple which is immutable and can be saved as key of dictionary
            key = tuple(sorted(ele))
            if key in ana_count:
                ana_count[key].append(ele)
            else:
                ana_count[key] = [ele]
        
        return ana_count.values()


# Efficient method
# O(m*n) time complexity   

def groupAnagrams(strs):

    res={}
        
    for s in strs:
        count=[0]*26 
                    
        for c in s:
            count[ord(c)-ord('a')]+=1            
            
        key=tuple(count)
        if key in res:
            res[tuple(count)].append(s)
        else:
            res[key]=[s]            
                
    return res.values()