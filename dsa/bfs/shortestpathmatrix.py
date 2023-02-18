from typing import List
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:         #self, grid: List[List[int]]) -> int:
        N = len(grid) #len
        q = deque([(0,0,1)]) #queue
        visit = set((0,0)) #setting 1st elem as visited
        dir = [[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    #        [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]


        while q:
            r,c,l = q.popleft()
            
            if (min(r,c) < 0 or max(r,c) >= N or grid[r][c]):
                continue
            if r == N-1 and c == N-1:
                print(l)
                return l
            for dr,dc in dir:
                if (r+dr,c+dc) not in visit:
                    q.append((r+dr,c+dc,l+1))
                    visit.add((r+dr,c+dc)) 

        return -1


# print(0<0)
f = Solution()
grid = [[0,1,1,0,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [1,0,1,1,0],
        [1,1,1,1,0]]
print(f.shortestPath(grid))