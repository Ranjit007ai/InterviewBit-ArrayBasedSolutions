def largest_no(A):
    # let's define a comparator function
    def comparator(A,B):
        # A and B are two numbers
        # for example A = 60 ,B =9 A>B
        # then AB  = 609 ,BA = 960 here, BA>AB
        AB = str(A) + str(B)
        BA = str(B) + str(A)
        return (int(AB) > int(BA)) - (int(AB) < int(BA))

    A = sorted(A,cmp=comparator) # cmp may not work in some python version
    if A.count(0) == len(A):
        return 0
    for i in range(0,len(A)):
        A[i] = str(A[i])
    return ''.join(A)

# checking the test case
A= [20,9,10] 
ans = largest_no(A)
print(ans) # the answer should be 92010