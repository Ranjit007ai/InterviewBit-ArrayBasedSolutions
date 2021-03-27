def max_abs_diff(A):
    # A is the list

    l = len(A)
    maxs = 0
    # we know the f(i,j) = |A[i]-A[j]| + |i-j|
    
    #traversing the list
    for i in range(0,l):
        for j in range(i,l):
            if i == j:
                abs_diff = 0
            else:
                abs_diff = abs(A[i] - A[j]) + abs(i - j)
            maxs = max(maxs,abs_diff)
    return maxs

# checking the test case
A = [1,3,-1]
ans = max_abs_diff(A)
print(ans)