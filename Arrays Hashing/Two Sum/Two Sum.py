def twoSum(nums, target):
        s=set()
        
        for i,value in enumerate(nums):
            r=target-nums[i]
            
            if r in s:
                return [i,nums.index(r)]
            s.add(value)

if __name__ == "__main__":
    arr=list(map(int,input().split()))
    target=int(input())
    print(twoSum(arr,target))
