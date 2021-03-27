def max_booking(A,B,k):
    A.sort()
    B.sort()
    for i in range(len(A)):
        if i + k < len(A) and A[i+k] < B[i]:
            return False
    return True

# checking the test case
A = [1,3,5]
B = [2,6,8]
k = 1
ans = max_booking(A,B,k)
print(ans)