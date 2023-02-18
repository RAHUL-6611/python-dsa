from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        out = 0
        kl=[]
        def avgfinder(al:List[int])-> bool:
            print(sum(al))
            if sum(al)/k >= threshold:
                return True

        for i in range(1,len(arr)-k):
            if (arr[i] >= threshold ):
                for j in range(k): #0 1 2
                    kl.append(arr[i+j])
                print(kl)
                if (avgfinder(kl)):            
                    out+=1

        return out


s = Solution()
print(
s.numOfSubarrays([2,2,2,2,5,5,5,8],3,4)
)