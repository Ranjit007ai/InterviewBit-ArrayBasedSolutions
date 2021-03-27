def max_subarray(Arr):
    # Arr is the list 
    # Initialization 
    l = len(Arr)
    temp_list = []
    max_list = []
    sums = 0
    maxs = 0
    neg_count = 0
    # let's Traverse the list
    for i in range(0,l):
        if Arr[i] >= 0:
            sums += Arr[i]
            temp_list.append(Arr[i])
        else:
            neg_count += 1
            if sums > maxs:
                maxs = sums
                max_list = temp_list
            elif sums == maxs:
                if len(temp_list) > len(max_list):
                    max_list = temp_list
            temp_list = []
            sums = 0
    if sums > maxs:
        maxs = sums
        max_list = temp_list
    if neg_count == l:
        return False

    return max_list

# checking on the test
Arr = [-1,-2,-5,-7,-2,-3]
ans = max_subarray(Arr)
print(ans)
                

        
