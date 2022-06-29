class Solution:
    # for encoding 
    def encode(self, strs):      
        res=''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res


    # for decoding the string
    
    def decode(self, str):
        res=[]
        i=0

        while i<len(str):
            j=i
            while str[j]!='#':
                j+=1
            lenght=int(s[i:j])
            res.append(str[j+1:j+1+lenght])
            i=j+1+lenght

        return res