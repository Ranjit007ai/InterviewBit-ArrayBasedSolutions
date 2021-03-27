def addone(A):
    # A is the list

    carry = 1
    # reversing the list
    A.reverse()
    # traversing the list
    for i  in range(0,len(A)):
        if carry == 0 :
            break
        sums = A[i] + carry
        A[i] = sums % 10
        carry = sums // 10
    if carry == 1:
        A.append(1)
    A.reverse()
    return A

# checking a test case
A = [9,9,9]
ans = addone(A)
print(ans)