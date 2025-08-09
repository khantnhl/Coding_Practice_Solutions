def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    left, right = 0, len(matrix)-1

    # layer by layer
    while(left < right):

        for i in range(right - left):

            top, bottom = left, right

            # save topleft
            topleft = matrix[top][left + i]

            # move bottom left to topleft
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right] 

            matrix[top + i][right] = topleft

        left += 1
        right -= 1

    return matrix