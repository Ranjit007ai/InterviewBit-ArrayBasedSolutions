def wave_array(A):
    
    
    for i in range(0,len(A)-1,2):
        if i == 0:
            if A[i] < A[i+1] :
                A[i] , A[i+1] = A[i+1] , A[i]
        else:
            if A[i] < A[i+1] :
                A[i] , A[i+1] = A[i+1] , A[i]
            if A[i] < A[i-1] :
                A[i] , A[i-1] = A[i-1], A[i]
    return A

# checking the test case
A = [6,7,5,3]
ans = wave_array(A)
print(ans)