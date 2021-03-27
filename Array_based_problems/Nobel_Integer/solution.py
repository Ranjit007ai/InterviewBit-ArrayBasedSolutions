def nobel_int(A):
    # A is the list
    # sorting the list
    A.sort()
    # traversing the list
    for i in range(0,len(A)-1):
        # in case of duplicates values
        if A[i] == A[i+1]:
            continue
        if A[i] == len(A) - i - 1:
            return True
    if A[-1] == 0:
        return True
    return False

# checking the test case
A = [2,3,4]
ans = nobel_int(A)
print(ans)


