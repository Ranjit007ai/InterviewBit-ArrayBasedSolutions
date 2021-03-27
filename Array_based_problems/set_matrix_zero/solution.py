def setzero(Mat,m,n):
    # Mat is the matrix
    
    rows = [False] * m 
    cols = [False] * n

    # traversing the matrix and if any row or col contain atleast one Zero then mark the coresponding position to true in rows and cols
    for i in range(0,m):
        for j in range(0,n):
            if Mat[i][j] == 0:
                rows[i] = True
                cols[j] = True
    # Again traversing the matrix to update
    for i in range(0,m):
        for j in range(0,n):
            if rows[i] == True or cols[j] == True:
                Mat[i][j] = 0
    return Mat

#checking the test case
Mat = [
        [1,0,1],
        [1,1,1],
        [0,1,1]
    ]
m = 3
n = 3
new_mat = setzero(Mat,m,n)
for i in range(0,m):
    for j in range(0,n):
        print(new_mat[i][j],end=' ')
    print('\n')