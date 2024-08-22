def moons_and_umbrellas():
    # Read input values
    X, Y, S = input().strip().split()
    X, Y = int(X), int(Y)
    
    # Initialize dp dictionary to store minimum cost for each character
    dp = {}
    prev_char = None  # To keep track of the previous character
    
    # Iterate through each character in the string S
    for current_char in S:
        new_dp = {}
        
        # Iterate through possible character pairs and their associated costs
        for char1, char2, cost in [('C', 'J', Y), ('J', 'C', X)]:
            if current_char == char2:
                new_dp[char1] = INF  # If current character is char2, set cost to infinity
            elif prev_char is None:
                new_dp[char1] = 0  # If no previous character, set cost to 0
            elif prev_char == char1:
                new_dp[char1] = dp[char1]  # If previous character is char1, carry forward the cost
            elif prev_char == char2:
                new_dp[char1] = dp[char2] + cost  # If previous character is char2, add the transition cost
            elif prev_char == '?':
                new_dp[char1] = min(dp[char1], dp[char2] + cost)  # If previous character is '?', take the minimum cost
        
        dp = new_dp  # Update dp with new_dp
        prev_char = current_char  # Update prev_char with current_char
    
    # Return the minimum value from dp dictionary
    return min(dp.values())

# Define infinity as a large number
INF = float("inf")

# Read the number of test cases
for case in range(int(input())):
    # Print the result for each test case
    print(f'Case #{case + 1}: {moons_and_umbrellas()}')