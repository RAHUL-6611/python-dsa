from typing import List
def dup2(nums: List[int],k:int)-> bool:
    window = set()
    L=0

    for R in range(len(nums)):
        if R-L > k:
            window.remove(nums[L])
            L+=1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False                        

print(dup2([1,0,1,1],1))