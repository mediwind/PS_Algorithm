import sys

def solve():
    """
    Solves a single test case for the Mod-3 Permutation problem.
    Calculates the minimum number of swaps required.
    """
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    # Counts for mismatches i_mod -> p_mod
    # cXY means index i has i % 3 == X and the value p[i] has p[i] % 3 == Y
    counts = [[0] * 3 for _ in range(3)]
    for i in range(n):
        i_mod = i % 3
        p_mod = p[i] % 3
        if i_mod != p_mod:
            counts[i_mod][p_mod] += 1
            
    c01 = counts[0][1]
    c02 = counts[0][2]
    c10 = counts[1][0]
    c12 = counts[1][2]
    c20 = counts[2][0]
    c21 = counts[2][1]

    # --- Calculate minimum swaps ---

    # Step 1: Perform direct swaps (Type 1 swaps)
    # Swap elements where i%3=X, p[i]%3=Y with elements where j%3=Y, p[j]%3=X
    swaps1_01_10 = min(c01, c10)
    swaps1_02_20 = min(c02, c20)
    swaps1_12_21 = min(c12, c21)
    
    swaps1 = swaps1_01_10 + swaps1_02_20 + swaps1_12_21

    # Step 2: Calculate remaining mismatches after direct swaps
    # These remaining mismatches must form cycles of length 3 (e.g., 0->1->2->0 or 0->2->1->0)
    rem_c01 = c01 - swaps1_01_10
    rem_c10 = c10 - swaps1_01_10
    # Only one of rem_c01 or rem_c10 can be non-zero. Their sum gives the number of remaining cycles.
    
    # The number of remaining cycles (k_rem) is the same regardless of which pair difference we calculate
    # k_rem = |c01 - c10| = |c02 - c20| = |c12 - c21|
    # We can calculate it as the sum of remaining mismatches for one direction pair
    k_rem = rem_c01 + rem_c10 # This equals |c01 - c10|

    # Step 3: Calculate swaps for remaining cycles (Type 2 swaps)
    # Each cycle of 3 mismatches (e.g., one 0->1, one 1->2, one 2->0) requires 2 swaps.
    swaps2 = 2 * k_rem

    # Total minimum swaps is the sum of type 1 and type 2 swaps
    total_swaps = swaps1 + swaps2
    
    return total_swaps

# Read the number of test cases
T = int(sys.stdin.readline())

# Process each test case
results = []
for i in range(1, T + 1):
    result = solve()
    results.append(f"Case #{i}: {result}")

# Print all results
print("\n".join(results))