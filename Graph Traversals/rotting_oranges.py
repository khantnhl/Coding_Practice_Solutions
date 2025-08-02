"""
    time : O(n * m)
    space: O(n * m)
"""

from typing import List

def orangesRotting(self, grid: List[List[int]]) -> int:
        
    rows, cols = len(grid), len(grid[0])
    from collections import deque
    queue = deque()
    fresh_bananas = 0
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if(grid[row][col]==1):
                fresh_bananas+=1
            elif(grid[row][col]==2):
                queue.append([row,col])
                visited.add((row,col))

    minutes = 0
    while(queue and fresh_bananas>0):
        for _ in range(len(queue)):
            r, c = queue.popleft()

            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            for rdr, cdr in directions:
                newRow = r + rdr
                newCol = c + cdr

                if(newRow<0 or newRow>=rows or newCol<0 or newCol>=cols or grid[newRow][newCol]!=1 or (newRow,newCol) in visited):
                    continue
                visited.add((newRow,newCol))
                queue.append((newRow,newCol))
                fresh_bananas-=1
        minutes+=1
    
    return minutes if(fresh_bananas==0) else -1