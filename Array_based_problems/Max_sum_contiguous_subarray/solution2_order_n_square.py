def max_subarray(A):
    l = len(A)
    sums = 0
    maxs = -9999999999
    for i in range(0,l):
        sums = 0
        for j in range(i,l):

            sums += A[j]
            maxs = max(sums,maxs)
    return maxs

# checking the test case
A = [-1,2,-3,4,1]
ans = max_subarray(A)
print(ans)    
            