def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    """ 
    [
        [1, 2, 4, 8],
        [10,11,12,13],
        [14,20,30,40]
    ], target = 10

    top =0, bottom =2
    check the boundaries

    """
    top, bottom = 0, len(matrix) - 1 # for rows
    while(top <= bottom):
        row = (top + bottom)//2
        if(target < matrix[row][0]):
            bottom = row - 1
        elif(target > matrix[row][-1]):
            top = row + 1
        else:
            break

    if(not top <= bottom):
        return False

    row = (top + bottom)//2
    left, right = 0, len(matrix[0]) - 1
    while(left <= right):
        mid = (left + right)//2
        if(target == matrix[row][mid]):
            return True
        elif(target < matrix[row][mid]):
            right = mid - 1
        else:
            left = mid + 1
    return False
