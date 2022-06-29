def minSwaps(s):
    maxClose,close=0,0    
    for c in s:
        if c=="[":
            close+=1
        else:
            close-=1
        maxClose=max(maxClose,close)

    return (maxClose+1)//2

if __name__ == '__main__':
    input_str=input()
    print(minSwaps(input_str))

