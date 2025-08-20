from collections import deque
from typing import List

"""
time : O(M * N * K)
space: O(M * N * K)

summary: 
    create 3D matrices for row,col, and obstacles.
    use 3D matrices for distance calculation and for checking visited 
    use BFS, explore four directions
"""

def shortestPath(self, grid: List[List[int]], k: int) -> int:

    ROWS, COLS = len(grid), len(grid[0])

    distance = [[[0 for _ in range(k + 1)] for c in range(COLS)] for r in range(ROWS)]
    visited = [[[False for _ in range(k + 1)] for c in range(COLS)] for c in range(ROWS)]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = True

    while(queue):
        curRow, curCol, curK = queue.popleft()

        # if this is the bottom right cell, return 
        if(curRow == ROWS-1 and curCol == COLS-1): 
            return distance[curRow][curCol][curK]

        # explore directions
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        for rdr, cdr in directions:
            newRow = curRow + rdr
            newCol = curCol + cdr
            
            # check bounds
            if(newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS):
                continue
            
            newK = curK
            if(grid[newRow][newCol]==1):
                newK += 1


            # can't go over k 
            if(newK > k): continue

            # if visited, skip
            if(visited[newRow][newCol][newK]): continue

            # update distance
            distance[newRow][newCol][newK] = distance[curRow][curCol][curK] + 1
            visited[newRow][newCol][newK] = True
            queue.append((newRow, newCol, newK))

    return -1