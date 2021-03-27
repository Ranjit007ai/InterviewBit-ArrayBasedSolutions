def r_and_m(A):
    n = len(A)
    # for  repeated twice  
    A.sort()
    for i in range(0,len(A)-1):
        if A[i] == A[i+1]:
            repeat = A[i]
            break
    # finding the missing number
    #mathematically if the no range from 1 to n , with 1 missing no .
    # missing_no = (sum(1-n) - sum(array)) + repeated

    # sum (1-n)
    n_sum = (n*(n+1))//2
    # sum of the list
    A_sum = sum(A)
    missing_no = (n_sum - A_sum) + repeat
    return missing_no,repeat

#checking the test case
A = [1,2,2,4]
m,r = r_and_m(A)
print('missing number',m)
print('repeated number',r)
