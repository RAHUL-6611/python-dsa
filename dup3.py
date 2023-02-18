from sortedcontainers import SortedList
    
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            # print(pos1)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)
            print(pos1,pos2)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([1,5,1,9,5,9],2,3))        