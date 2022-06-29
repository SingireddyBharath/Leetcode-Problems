
# using Dictionary
# O(n) time complexity.

def NoOfsubarrSum(arr,k):
    mymap={}
    currSum=0
    cnt=0
    for i in range(len(arr)):
        currSum += arr[i]
        if currSum==k:
            cnt+=1
        if currSum-k in mymap.keys():
            cnt+=mymap[currSum-k] 
        if currSum in mymap:
            mymap[currSum] += 1
        else:
            mymap[currSum]=1

    return cnt

if __name__ == '__main__':
    arr=list(map(int,input().split()))
    k=int(input())
    print(NoOfsubarrSum(arr,k))       
    
