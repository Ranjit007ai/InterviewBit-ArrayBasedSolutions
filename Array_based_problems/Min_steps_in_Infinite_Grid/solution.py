def min_steps(X,Y):
    # X is the list having the X-coordinates
    # Y is the list having the correspounding Y-Coordinates
    steps = 0
    for i in range(0,len(X)-1):
        steps += min(abs(X[i]-X[i+1]),abs(Y[i]-Y[i+1]))
        steps += abs(abs(X[i]-X[i+1]) - abs(Y[i]-Y[i+1]))
    return steps

# checking the test case
X = [0,1,1]
Y = [0,1,2]
ans = min_steps(X,Y)
print(ans)