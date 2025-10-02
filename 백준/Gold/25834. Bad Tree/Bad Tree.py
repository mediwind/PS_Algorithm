def solve():
    try:
        n, k = map(int, input().split())
    except (IOError, ValueError):
        return

    if n > 1 and n <= 64:
        max_k = 1 << (n - 1)
        if k > max_k:
            print(-1)
            return
    elif n == 1:
        if k > 1:
            print(-1)
            return

    result = []
    low = 1
    high = n

    for i in range(n):
        remaining_count = n - i
        
        if remaining_count == 1:
            result.append(low)
            break
        
        if remaining_count - 2 >= 64:
            permutations_with_low = float('inf')
        else:
            permutations_with_low = 1 << (remaining_count - 2)

        if k <= permutations_with_low:
            result.append(low)
            low += 1
        else:
            result.append(high)
            high -= 1
            k -= permutations_with_low
            
    print(*result)

solve()