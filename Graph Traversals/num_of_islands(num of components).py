"""
    time : O(v + e)
    space: O(v)
"""

def numIslands(self, grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    numofIslands=0

    def dfs(row, col):

        visited.add((row,col))
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        for rdr,cdr in directions:
            newRow = rdr + row
            newCol = cdr + col

            if(0<=newRow<rows and 0<=newCol<cols and (newRow,newCol) not in visited and grid[newRow][newCol]=="1"):
                dfs(newRow, newCol)

        return

    for row in range(rows):
        for col in range(cols):
            if(grid[row][col]=="1" and (row,col) not in visited):
                dfs(row, col)   
                numofIslands+=1

    return numofIslands