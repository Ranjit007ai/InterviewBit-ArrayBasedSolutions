def spiral(A):
    # A is the integer
    # we need to create a matrix whose element range from 1 to A^2 in spiral order
    # creating a Zeros matrix of size A*A
    Mat = [[0]*A for i in range(0,A)]
    value = 1 # value range from 1 to A^2
    start_row = 0
    end_row = A - 1
    start_col = 0
    end_col = A - 1
    # traversing the matrix in the spiral order
    while start_row <= end_row and start_col <= end_col :
        # moving left to right
        if start_col <= end_col:
            for col in range(start_col,end_col+1):
                Mat[start_row][col] = value
                value += 1
            start_row += 1
        else:
            break
        # moving top to bottom
        if start_row <= end_row:
            for row in range(start_row,end_row+1):
                Mat[row][end_col] = value
                value += 1
            end_col -= 1
        else:
            break
        # moving from right to left
        if end_col >= start_col :
            for col in range(end_col,start_col - 1,-1):
                Mat[end_row][col] = value
                value += 1
            end_row -= 1
        else:
            break
        # moving bottom to top
        if end_row >= start_row:
            for row in range(end_row,start_row-1,-1):
                Mat[row][start_col] = value
                value += 1
            start_col += 1
        else:
            break
    return Mat

# checking the test case
A = 3
mat = spiral(A)
for i in range(0,A):
    for j in range(0,A):
        print(mat[i][j],end=' ')
    print(end='\n')

        