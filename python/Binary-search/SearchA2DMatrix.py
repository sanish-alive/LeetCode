
def searchMatrix(matrix, target):
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        if(matrix[i][0]<=target and matrix[i][column-1]>=target ):
            for j in range(column):
                if matrix[i][j] == target:
                    return True
    return False


matrix = [[1]]
target = 1
print(searchMatrix(matrix, target))