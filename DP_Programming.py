def unbound_knapsack(value, weight, W):
    n = len(weight)
    sack_weight = [0] * (W + 1) 

    #populate weight array 
    for current_weight in range(1, W + 1):
        #iterate through each item
        for i in range(n):
            #check if adding the current item increases sack weight 
            if weight[i] <= current_weight and (sack_weight[current_weight - weight[i]] + value[i]) > sack_weight[current_weight]:
                sack_weight[current_weight] = sack_weight[current_weight - weight[i]] + value[i]

    return sack_weight[W]

weights = [2, 4, 6]
values = [20, 45, 55]
max_w = 9
print("Maximum weight of knapsack: " + str(unbound_knapsack(values, weights, max_w)))



def weighted_interval_scheduling(s, f, v):
    #combine and sort into tuples
    intervals = sorted(zip(s, f, v), key=lambda x: x[1])

    n = len(intervals)
    interval_weights = [0] * (n + 1)

    #use binary search to find interval 
    def find_non_overlapping(i):
        left, right = 0, i - 1 #set pointers to start and end 
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][1] <= intervals[i][0]:
                if mid + 1 <= right and intervals[mid + 1][1] <= intervals[i][0]:
                    left = mid + 1
                else:
                    return mid
            else:
                right = mid - 1
        return -1  

    #find the maximum values of non-overlapping intervals
    for i in range(1, n + 1):
        #find last non overlapping interval
        non_overlap_index = find_non_overlapping(i - 1)
        # either include interval or not 
        if interval_weights[i - 1] < (intervals[i - 1][2] + interval_weights[non_overlap_index + 1]):
            interval_weights[i] = intervals[i - 1][2] + interval_weights[non_overlap_index + 1]
        else:
            interval_weights[i] = interval_weights[i - 1]

    return interval_weights[n]

s = [1, 3, 5, 6, 9, 10]
f = [4, 4, 7, 8, 11, 11]
v = [5, 7, 10, 4, 10, 4]
print("Maximum weight of schedule: " + str(weighted_interval_scheduling(s, f, v)))


def max_profit(k, prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    #2d array to store cases
    profits = [[0] * n for _ in range(k + 1)]

    #iterate through number of transactions
    for t in range(1, k + 1):
        max_diff = -prices[0]
        # go through each day of prices, see if we should add it to current transaction
        for d in range(1, n):
            profits[t][d] = max(profits[t][d-1], prices[d] + max_diff)
            max_diff = max(max_diff, profits[t-1][d] - prices[d])

    return profits[k][n-1]

prices = [3, 5, 8, 2, 4, 10, 1, 3]
k = 2
print("Maximum profit of transactions: " + str(max_profit(k, prices)))

def countWaysToMakeChange(coins, n):
    m = len(coins)  # length of coins array

    # Create a 2D array of size (m+1) x (n+1) and initialize all values to 0
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case: there is one way to make change for 0, which is to use no coins
    for i in range(m + 1):
        dp[i][0] = 1

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(n + 1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[m][n]

# Example Usage
coins = [1, 2, 5]  # example coin denominations
n = 11  # target amount
result = countWaysToMakeChange(coins, n)
print("Number of ways to make change:", result)
