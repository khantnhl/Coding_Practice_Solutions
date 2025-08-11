
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

def revert_row(matrix):
    for row in matrix:
        row.reverse()
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))
print(revert_row(matrix))

"""
[1,2,3] (0,1) -> (0,1)
[4,5,6]
[7,8,9]

[1,4,7]
[2,5,8]
[3,6,9]
"""