# lets say there are m tripet for sum < b
# lets say there are n triplet for sum < a
# so ,triplet in bw a and b are (m-n)
def triplet(A,val):
    # A is the list
    # val is the value below which the the triplet 
    i =0
    j = 0
    k = 0
    n = len(A)
    count = 0
    # sorting the list A
    A.sort()
    for i in range(0,n-2):
        j = i + 1 # start index
        k = n - 1 # end_index
        while j != k:
            sums = A[i] + A[j] + A[k]
            if sums > val:
                k -= 1
            else:
                count += (k-j)
                j += 1
    return count


# total no of triplet b/w 1 and 2
A = [0.6,0.7,0.8,1.2,0.4]
res = triplet(A,2) - triplet(A,1)
print(res)

    