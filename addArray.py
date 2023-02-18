from typing import List

def addArr(nums:List[int],k:int)->List[int]:
    nums.reverse()
    i=0
    while k:
        take = k%10
        if(i < len(nums)):
            nums[i] += take
        else:
            nums.append(take)
        carry = nums[i] // 10
        nums[i] = nums[i]%10
        k = k //10
        k+= carry
        i+=1
    nums.reverse()
    for j in nums:
        print(j)
    


addArr([1,5,9,0,1],34)  
