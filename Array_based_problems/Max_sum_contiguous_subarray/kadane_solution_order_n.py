def max_subarray(A):
    ans = 0
    sums = 0
    neg_count = 0
    for i in range(0,len(A)):
        if A[i] < 0:
            neg_count += 1
        if sums + A[i] > 0:
            sums += A[i]
        else:
            sums = 0
        ans = max(sums,ans)
    if neg_count == len(A):
        return max(A)
    return ans

# checking test case
A =[-1,-3,-2]
ans = max_subarray(A)
print(ans)