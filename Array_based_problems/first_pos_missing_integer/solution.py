# the first + no is 1
# if all the no is - ,they return 1
# check if the 1 is present or not 
# if there is no missing no then return the next element after the list
# ** we need to take care of positive integer only

def missing(A):
    #  A is the list
    # sort the list
    A.sort()
    # checking if all no are negative ,if yes then return 1
    if A[-1] < 0:
        return 1
    # if there is no 1 in the list
    if A.count(1) == 0:
        return 1
    #traversing the list
    for i in range(0,len(A)-1):
        if A[i] > 0 and A[i+1] > 0: # if they are positive
            if A[i+1] - A[i] > 1 :
                return A[i] + 1

    
    return A[-1] + 1 # if all the no are present then return next number of the last no

# checking the testcase
A = [1,2,4,5]
ans = missing(A)
print(ans)