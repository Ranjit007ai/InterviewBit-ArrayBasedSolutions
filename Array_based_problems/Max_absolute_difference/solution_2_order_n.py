def max_abs_diff(A):
    # A[i]+i
    # -A[i]+i
    max_1 = -99999999999
    max_2 = -99999999999
    min_1 = 999999999999
    min_2 = 999999999999

    for i in range(0,len(A)):
        max_1 = max(max_1,A[i]+i)
        max_2 = max(max_2,-A[i]+i)
        min_1 = min(min_1,A[i]+i)
        min_2 = min(min_2,-A[i]+i)
    max_ans = max(max_1-min_1,max_2-min_2)
    return max_ans

#checking the test case
A = [1,3,-1]
ans = max_abs_diff(A)
print(ans)