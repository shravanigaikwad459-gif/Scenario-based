# Fibonacci Sequence Using Memoization (Top-Down Dynamic Programming)

# Accept an integer N
n = int(input("Enter the number of terms (N): "))


# Helper function to compute Fibonacci with memoization
def fibonacci(k, memo):
    if k in memo:
        return memo[k]

    # Base cases
    if k == 0:
        return 0
    if k == 1:
        return 1

    # Recurrence relation with memoization
    memo[k] = fibonacci(k - 1, memo) + fibonacci(k - 2, memo)
    return memo[k]


# Handle non-positive input
if n <= 0:
    print("Please enter a positive integer.")
else:
    memo = {}
    sequence = []

    # Generate the first N Fibonacci numbers
    for i in range(n):
        sequence.append(fibonacci(i, memo))

    print(f"First {n} Fibonacci numbers = {sequence}")
