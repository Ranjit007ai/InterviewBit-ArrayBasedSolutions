def pascal(nums_rows):
    # nums_rows is the total no of row in the pascal triangle
    # creating a pascal triangle with 0 initially
    tri = [[0]*k for k in range(1,nums_rows+1)]

    # traversing the tri
    for row in range(0,nums_rows):
        for col in range(0,row + 1):
            if col == 0 or col == (row):
                tri[row][col] = 1
            else:
                tri[row][col] = tri[row-1][col-1] + tri[row-1][col]
    return tri


# checking the test case
num_rows = 5
ans = pascal(num_rows)
for row in range(0,num_rows):
    for col in range(0,row+1):
        print(ans[row][col],end=' ')
    print('\n')
