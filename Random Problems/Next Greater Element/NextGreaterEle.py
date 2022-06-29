# Brute force algorithm
# O(n^2) time complexity

def findNextGreaterElements(input):
    
    res=[]  #result array
    # do for each element
    for i in range(len(input)):
        # keep track of the next greater element for element `input[i]`
        next = -1
        # process elements on the right of element `input[i]`
        for j in range(i + 1, len(input)):
            # break the inner loop at the first larger element on the
            # right of element `input[i]`
            if input[j] > input[i]:
                next=input[j]                
                break

        res.append(next)

    return res
 
 
# Using Stack 
# O(n) time complexity

def findNextGreaterElements(arr):

    stack=[0]
    res=[-1 for i in range(len(arr))] 
    for i in range(1,len(arr)):
        if not stack:
            stack.append(i)    
        while stack and arr[stack[-1]]<arr[i]:
                res[stack[-1]]=arr[i]
                stack.pop()
        stack.append(i)

    return res


# Driver code
if __name__ == '__main__':
     
    input = list(map(int,input().split()))
    print(findNextGreaterElements(input))
