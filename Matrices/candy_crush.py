"""
1. using horizonal and vertical scanning negate the values if three or more values are same
2. Swap if the values are positives using pointer
3. Place Zeros to the rest
"""

def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

    ROWS, COLS = len(board), len(board[0])

    shouldCrush = True

    while(shouldCrush):
        shouldCrush = False # reset

        # horizontal scanning
        for row in range(ROWS):
            for col in range(COLS - 2):
                candy_val = abs(board[row][col])
                if(candy_val != 0 and 
                   candy_val == board[row][col + 1] == board[row][col + 2]):
                    shouldCrush = True
                    board[row][col] = -candy_val    # negate values
                    board[row][col + 1] = -candy_val
                    board[row][col + 2] = -candy_val
        
        for col in range(COLS):
            for row in range(ROWS - 2):
                candy_val = abs(board[row][col])
                if(candy_val != 0 and 
                   candy_val == board[row][col + 1] == board[row][col + 2]):
                    shouldCrush = True
                    board[row][col] = -candy_val    # negate values
                    board[row][col + 1] = -candy_val
                    board[row][col + 2] = -candy_val
    
    # if flagged
    if(shouldCrush):
        for col in range(COLS):
            writeHere = ROWS - 1

            for row in range(ROWS - 1, -1, -1):
                if(board[row][col] > 0):
                    board[writeHere][col] = board[row][col]
                    writeHere -= 1

            while(writeHere >= 0):
                board[writeHere][col] = 0 # place zero after dropping candies
                writeHere -= 1
    
    return board