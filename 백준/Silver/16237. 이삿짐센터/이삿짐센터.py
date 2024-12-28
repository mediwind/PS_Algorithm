def min_baskets(A, B, C, D, E):
    weights = {1: A, 2: B, 3: C, 4: D, 5: E}
    baskets = 0
    
    while sum(weights.values()) > 0:
        current_weight = 0
        for weight in range(5, 0, -1):
            while weights[weight] > 0 and current_weight + weight <= 5:
                current_weight += weight
                weights[weight] -= 1
        baskets += 1
    
    return baskets


A, B, C, D, E = map(int, input().split())
print(min_baskets(A, B, C, D, E))