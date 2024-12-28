def min_baskets(A, B, C, D, E):
    weights = [1] * A + [2] * B + [3] * C + [4] * D + [5] * E
    weights.sort(reverse=True)
    
    baskets = 0
    while weights:
        current_weight = 0
        i = 0
        while i < len(weights):
            if current_weight + weights[i] <= 5:
                current_weight += weights[i]
                weights.pop(i)
            else:
                i += 1
        baskets += 1
    
    return baskets


A, B, C, D, E = map(int, input().split())
print(min_baskets(A, B, C, D, E))