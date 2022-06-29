# O(n) time complexity

def topKFrequent(nums,k):
        d={}        
        for key in nums:
            
            if key in d:
                d[key]+=1
            else:
                d[key]=1
                
        res=[]    
          
        d=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        
        for i in d:
            res.append(i)
            if len(res)==k:
                break

        return res