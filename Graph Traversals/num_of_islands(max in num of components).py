"""
    time : O(v + e)
    space: O(v)
"""
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
    rows,cols = len(grid), len(grid[0])
    num_of_islands=0
    visited = set()
    maxT = 0
    def dfs(row,col):
        #Base
        if(row < 0 or row >=rows or col < 0 or col>=cols or grid[row][col]==0 or (row,col) in visited):
            return 0

        visited.add((row,col))
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        area = 1
        for rdr, cdr in directions:
            newRow = rdr + row
            newCol = cdr + col 

            if(0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]==1 and (newRow,newCol) not in visited):
                area += dfs(newRow, newCol) # 1 + 1 + 1....
            
        return area

    for row in range(rows):
        for col in range(cols):
            if((row,col) not in visited and grid[row][col]==1):
                curarea = dfs(row,col)
                maxT = max(maxT, curarea)

    return maxT
