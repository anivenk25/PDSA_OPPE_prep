def domino_solitaire(N, grid):
    # Initialize the dp array with -inf values
    dp = [-float('inf')] * (N + 1)
    
    # Base case: no columns covered
    dp[0] = 0
    
    # Iterate over the columns from 1 to N
    for i in range(1, N + 1):
        # Vertical domino at column i
        dp[i] = dp[i-1] + abs(grid[0][i-1] - grid[1][i-1])
        
        # Horizontal domino covering columns (i-1, i), if i > 1
        if i > 1:
            dp[i] = max(dp[i], dp[i-2] + abs(grid[0][i-2] - grid[0][i-1]) + abs(grid[1][i-2] - grid[1][i-1]))
    
    # The result is the maximum score for the entire grid
    return dp[N]

# Input reading
N = int(input())  # Number of columns in the grid
grid = []
for _ in range(2):
    grid.append(list(map(int, input().split())))

# Calculate the maximum score
print(domino_solitaire(N, grid))

