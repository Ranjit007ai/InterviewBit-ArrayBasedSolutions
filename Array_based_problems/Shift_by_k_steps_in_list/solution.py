# function to shift the element in the list by k steps
def shift(A,k):
    l = len(A)
    k= k % l 
    A = A[k:] + A[:k] 
    return A

# checking a test case
A = [3,4,1,2]
new_A = shift(A,10)
print('Orignial List',A)
print('List after shifting',new_A)
