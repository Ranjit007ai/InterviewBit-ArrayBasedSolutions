def repeat(A):
    n = len(A)
    r = n//3
    count = 0
    A.sort()
    for i in range(0,n-1):
        if A[i] == A[i+1]:
            count += 1
        else:
            if (count + 1) > r :
                return A[i-1]
            else:
                count = 0

    if (count + 1) > r:
        return A[-1]
    return -1
# checking the test case
A = [1,1,1,4]
ans = repeat(A)
print(ans)
