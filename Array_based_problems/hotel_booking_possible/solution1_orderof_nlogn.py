def max_booking(arrival,departure,n,k):
    ans = []
    for i in range(0,n):
        ans.append((arrival[i],1))
        ans.append((departure[i],0))
    
    ans.sort()
    cur_active = 0
    max_active = 0
    for i in range(0,len(ans)):
        if ans[i][1] == 1:
            cur_active += 1
            max_active = max(max_active,cur_active)
        else:
            cur_active -= 1
    # if max active guest at any instance are more than avaiable rooms,return false,else return true
    return (k>=max_active)

# checking test case
arrival = [1,3,5]
departure = [2,6,8]
ans = max_booking(arrival,departure,3,1)
print(ans)