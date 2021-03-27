# here we need to print the matrix elements in the form of Spiral Order
def spiralordermatrix(Mat,m,n):
    # Mat is the matrix 
    # m is the no of rows in the matrix
    # n is the no of columns in the matrix
    
    # Initializing some variables
    li = []
    start_row = 0 #
    end_row = m - 1 # last index of row
    start_col = 0
    end_col = n -1 # last index of col

    while start_row<=end_row and start_col<=end_col:
        # moving from Left to Right
        if start_col <= end_col :
            for col in range(start_col,end_col+1):
                li.append(Mat[start_row][col])
            
            start_row += 1
        else:
            break
        # moving from top to bottom
        if start_row <= end_row:
            for row in range(start_row,end_row+1):
                li.append(Mat[row][end_col])
            
            end_col -= 1 
        else:
            break
        
        # moving from right to left
        if end_col >=start_col:
            for col in range(end_col,start_col-1,-1):
                li.append(Mat[end_row][col])
            
            end_row -= 1
        else:
            break
        
        # moving from bottom to top
        if end_row >= start_row:
            for row in range(end_row,start_row-1,-1):
                li.append(Mat[row][start_col])
            
            start_col += 1
        else:
            break
    return li

# checking a test case

Mat = [[1,2,3],[4,5,6],[7,8,9]]
m = 3
n = 3
ans = spiralordermatrix(Mat,m,n)
print(ans)

