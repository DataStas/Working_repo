
import numpy as np

maxSum = 100
arrSize = 51

dp = np.zeros((arrSize, maxSum));
visit = np.zeros((arrSize, maxSum));
def SubsetCnt(i, s, arr, n) :
     
    # Base cases
    if (i == n) :
        if (s == 0) :
            return 1;
        else :
            return 0;
     
    # Returns the value
    # if a state is already solved
    if (visit[i][s + arrSize]) :
        return dp[i][s + arrSize];
 
    # If the state is not visited,
    # then continue
    visit[i][s + arrSize] = 1;
 
    # Recurrence relation
    dp[i][s + arrSize ] = (SubsetCnt(i + 1, s + arr[i], arr, n) +
                           SubsetCnt(i + 1, s, arr, n));
 
    # Returning the value
    return dp[i][s + arrSize];
 
# Driver Code
if __name__ == "__main__" :
 
    arr = [42, -42, 42]
    n = len(arr);
 
    print(SubsetCnt(0, 0, arr, n));
