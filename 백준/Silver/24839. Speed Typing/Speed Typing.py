def solve_case():
    # Read input strings
    initial_string = input()
    target_string = input()
    
    # Create dictionaries to count occurrences of each character
    initial_count = {}
    target_count = {}
    
    # Count characters in initial_string
    for char in initial_string:
        initial_count[char] = initial_count.get(char, 0) + 1
    
    # Count characters in target_string
    for char in target_string:
        target_count[char] = target_count.get(char, 0) + 1
    
    # Convert strings to sets to check for impossible cases
    initial_set = set(initial_string)
    target_set = set(target_string)
    
    # If there are characters in initial_string not in target_string, return "IMPOSSIBLE"
    if initial_set - target_set:
        return "IMPOSSIBLE"
    
    # Check if target_string has enough characters to match initial_string
    for char in initial_count:
        if target_count.get(char, 0) < initial_count[char]:
            return "IMPOSSIBLE"
    
    # Two-pointer technique to check if initial_string can be formed from target_string
    i, j = 0, 0
    match_count = 0
    while i < len(initial_string) and j < len(target_string):
        if initial_string[i] == target_string[j]:
            i += 1
            match_count += 1
        j += 1
    
    # If not all characters of initial_string are matched, return "IMPOSSIBLE"
    if match_count != len(initial_string):
        return "IMPOSSIBLE"
    else:
        # Return the number of extra characters in target_string
        return len(target_string) - len(initial_string)

# Read number of test cases
T = int(input())
for t in range(1, T + 1):
    print(f"Case #{t}: " + str(solve_case()))