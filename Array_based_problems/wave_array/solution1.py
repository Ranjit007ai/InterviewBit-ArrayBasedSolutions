# A[1]>=A[2]<=A[3]>=A[4]<=A[5]....
def wave_array(A):
    # A is the list
    # the idea is the sort the list A in ascending order
    # swap the adjacent elements

    A.sort()
    for i in range(0,len(A)-1,2):
        A[i],A[i+1] = A[i+1], A[i]
    return A

# checking the test case
A = [6,7,5,3]
ans = wave_array(A)
print(ans)
