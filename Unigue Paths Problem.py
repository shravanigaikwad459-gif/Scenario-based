# Unique Paths Problem using Dynamic Programming

# Accept number of rows and columns
rows, cols = map(
    int, input("Enter number of rows and columns (e.g., 3 7): ").split()
)

# Handle edge cases (empty grid or single point)
if rows <= 0 or cols <= 0:
    print("Total number of unique paths = 0")
elif rows == 1 or cols == 1:
    print("Total number of unique paths = 1")
else:
    # dp[i][j] stores the number of unique paths to reach cell (i, j)
    dp = [[0] * cols for _ in range(rows)]

    # Base case: There is only 1 way to reach any cell in the first row or first column
    for i in range(rows):
        dp[i][0] = 1
    for j in range(cols):
        dp[0][j] = 1

    # Fill the DP table
    for i in range(1, rows):
        for j in range(1, cols):
            # Paths to (i, j) = paths from above + paths from left
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print("Total number of unique paths =", dp[rows - 1][cols - 1])
