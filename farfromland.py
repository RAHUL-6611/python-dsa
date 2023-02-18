from typing import List
from collections import deque

def maxDistance(grid:List[List[int]]) -> int:
    N = len(grid)
    q = deque()

    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                q.append([r,c])

    od = [[0,1],[1,0],[0,-1],[-1,0]]
    res=-1
    while q:
        r,c = q.popleft()
        res = max(res,grid[r][c])
        for dr,dc in od:
            newr,newc = dr+r,dc+c
            if (min(newr,newc)>=0 and max(newr,newc)<N and grid[newr][newc]==0):
                q.append([newr,newc])
                grid[newr][newc] = grid[r][c]+1

    return res-1 if res>1 else -1


island = [[1,0,1],
            [0,0,0],
            [1,0,0]]

print(maxDistance(island))
