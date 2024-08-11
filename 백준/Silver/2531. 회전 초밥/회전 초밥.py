import sys
input = sys.stdin.readline

# Read input values
num_plates, num_sushi_types, num_consecutive_plates, coupon_sushi = map(int, input().rstrip().split())

# Initialize the sushi array
sushi_plates = [int(input()) for _ in range(num_plates)]

# Initialize the maximum number of different sushi types that can be eaten
max_sushi_types = 0

# Iterate over each possible starting point for the consecutive plates
for start in range(num_plates):
    if start + num_consecutive_plates > num_plates:
        # If the window exceeds the array bounds, wrap around using modulo
        current_sushi_set = set(sushi_plates[start:num_plates] + sushi_plates[:(start + num_consecutive_plates) % num_plates] + [coupon_sushi])
    else:
        # If the window is within the array bounds
        current_sushi_set = set(sushi_plates[start:start + num_consecutive_plates] + [coupon_sushi])
    
    # Calculate the number of different sushi types in the current window
    number_of_types = len(current_sushi_set)
    
    # Update the maximum number of different sushi types that can be eaten
    if max_sushi_types < number_of_types:
        max_sushi_types = number_of_types

# Print the result
print(max_sushi_types)