# time : O(n*m)
# space : O(n*m)

"""
start from right to left
swap if stones
move pointer if it is obstable
start collecting from bottom to top since 90deg rotated
"""

def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

    """
    [["#","#","*",".","*","."],
    ["#","#","#","*",".","."],
    ["#","#","#",".","#","."]]
                        i   c

    """
    ROWS, COLS = len(boxGrid), len(boxGrid[0])

    for row in range(ROWS):
        idx = COLS - 1 # the end of columns
        for col in range(COLS-1, -1, -1):
            if(boxGrid[row][col]=="#"):
                # swap 
                boxGrid[row][col], boxGrid[row][idx] = boxGrid[row][idx], boxGrid[row][col]
                idx -= 1
            elif(boxGrid[row][col]=="*"):
                idx = col - 1

    result = []
    for col in range(COLS):
        hold = []
        # bottom to top
        for row in range(ROWS-1, -1,-1):
            hold.append(boxGrid[row][col])
        result.append(hold)
    return result

                
