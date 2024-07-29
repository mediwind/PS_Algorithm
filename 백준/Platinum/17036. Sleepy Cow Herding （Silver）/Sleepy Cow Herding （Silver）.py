import sys
input = sys.stdin.readline

num_cows = int(input())
herd_positions = sorted(int(input()) for _ in range(num_cows))

# Initialize minimum moves to infinity
min_moves = float("inf")

# Check special cases for minimum moves
if herd_positions[num_cows - 2] - herd_positions[0] == num_cows - 2 and herd_positions[num_cows - 1] - herd_positions[num_cows - 2] > 2:
    min_moves = 2
elif herd_positions[num_cows - 1] - herd_positions[1] == num_cows - 2 and herd_positions[1] - herd_positions[0] > 2:
    min_moves = 2
else:
    # Calculate minimum moves by finding the patch of length n with the least number of gaps
    farthest_cow_index = 0
    for current_cow_index in range(num_cows):
        while farthest_cow_index + 1 < num_cows and herd_positions[farthest_cow_index + 1] - herd_positions[current_cow_index] < num_cows:
            farthest_cow_index += 1
        min_moves = min(min_moves, num_cows - (farthest_cow_index - current_cow_index + 1))

# Calculate the number of empty cells (gaps) between cows
total_gaps = 0
for current_cow_index in range(1, num_cows):
    total_gaps += herd_positions[current_cow_index] - herd_positions[current_cow_index - 1] - 1

# Calculate maximum moves as the maximum of the total gaps minus either the first or last gap
max_moves = max(
    total_gaps - (herd_positions[1] - herd_positions[0] - 1), 
    total_gaps - (herd_positions[num_cows - 1] - herd_positions[num_cows - 2] - 1)
)

# Output the results
print(min_moves)
print(max_moves)