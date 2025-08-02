"""
time : O(n*m)
space: O(n*m)
"""
from typing import List

def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
    rows, cols = len(grid), len(grid[0])
    from collections import deque
    queue = deque()
    visited = set()

    # get all treasures to queue
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col]==0):
                queue.append((row,col))
                visited.add((row,col))
    

    # multi-source BFS
    distance = 0
    while(queue):
        for _ in range(len(queue)):
            r, c = queue.popleft()

            grid[r][c] = distance 

            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            for rdr, cdr in directions:
                newRow = rdr + r
                newCol = cdr + c

                # check bounds
                if(newRow<0 or newRow>=rows or newCol<0 or newCol>=cols
                    or (newRow,newCol) in visited or grid[newRow][newCol]==-1):
                    continue

                visited.add((newRow, newCol))
                queue.append([newRow,newCol])

        distance += 1 # increment for each level of BFS