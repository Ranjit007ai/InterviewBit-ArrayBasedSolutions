def anti_diagonal(A):
    n = len(A)
    temp = []
    li = []
    # column wise
    for col in range(0,n):
        i = col
        for row in range(0,n):
            if i >= 0:
                temp.append(A[row][i])
                i -= 1
            else:
                break
        li.append(temp)
        temp = []

    # row wise
    for row in range(1,n):
        i = row
        for col in range(n-1,0,-1):
            if i < n:
                temp.append(A[i][col])
                i += 1
            else:
                break
        li.append(temp)
        temp = []
    return li

# checking the test case
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
ans = anti_diagonal(A)
for i in range(0,len(ans)):
    print(ans[i])
