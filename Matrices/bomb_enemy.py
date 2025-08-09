"""
time : O(n * m)
"""

def maxKilledEnemies(self, grid: List[List[str]]) -> int:
    
    ROWS, COLS = len(grid), len(grid[0])

    res_grid = [[0] * len(grid[0]) for _ in range(len(grid))]

    # left to right
    for i in range(ROWS):
        kill_count = 0
        for j in range(COLS):
            if(grid[i][j] =="W"):
                kill_count = 0
            elif(grid[i][j]=="E"):
                kill_count += 1
            else:
                res_grid[i][j] += kill_count

        kill_count = 0
        for j in range(COLS-1,-1,-1):
            if(grid[i][j] =="W"):
                kill_count = 0
            elif(grid[i][j]=="E"):
                kill_count += 1
            else:
                res_grid[i][j] += kill_count

    # top to bottom
    for i in range(COLS):
        kill_count = 0
        for j in range(ROWS):
            if(grid[j][i] =="W"):
                kill_count = 0
            elif(grid[j][i]=="E"):
                kill_count += 1
            else:
                res_grid[j][i] += kill_count
        
        kill_count = 0
        for j in range(ROWS-1,-1,-1):
            if(grid[j][i] =="W"):
                kill_count = 0
            elif(grid[j][i]=="E"):
                kill_count += 1
            else:
                res_grid[j][i] += kill_count
    max_result = max(
        [res_grid[i][j] for i in range(ROWS) for j in range(COLS)], default=0
    )

    return max_result