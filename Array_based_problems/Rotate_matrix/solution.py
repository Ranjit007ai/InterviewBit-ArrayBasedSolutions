# the matrix after rotation of 90 degree clockwise is same as
# Transposing the matrix
# reversing each row

def rotation(Mat):
    # Transposing the matrix
    for i in range(0,len(Mat)):
        for j in range(i,len(Mat[0])):
            Mat[i][j] , Mat[j][i] = Mat[j][i] , Mat[i][j]
    # reversing each row 
    for i in range(0,len(Mat)):
        Mat[i].reverse()
    return Mat

# checking the test case
Mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
rotated_matrix = rotation(Mat)
for i in range(0,len(rotated_matrix)):
    for j in range(0,len(rotated_matrix[0])):
        print(rotated_matrix[i][j],end=' ')
    print(end='\n')