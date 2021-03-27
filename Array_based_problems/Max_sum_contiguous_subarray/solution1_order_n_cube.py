def max_subarray(Arr):
    maxs = -99999999999
    l = len(Arr)
    for sub_ar_size in range(1,l+1):
        for start_pos in range(0,l):
            sums = 0
            if start_pos + sub_ar_size - 1 >= l:
                break 
            for curr in range(start_pos,start_pos + sub_ar_size):
                sums += Arr[curr]
            if sums > maxs:
                maxs = sums
    return maxs

# checking the test case
A = [-1,-2,3,5]
ans = max_subarray(A)
print(ans)
