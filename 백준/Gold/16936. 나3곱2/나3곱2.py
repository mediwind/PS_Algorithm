def find_sequence(n, numbers):
    result = list()

    first_value = numbers[0]
    max_power = 0

    for i in range(n):
        temp = numbers[i]
        power = 0
        while temp % 3 == 0:
            temp //= 3
            power += 1
        if (power > max_power) or (power == max_power and numbers[i] < first_value):
            max_power = power
            first_value = numbers[i]

    result.append(first_value)

    for i in range(n):
        if result[-1] * 2 in numbers:
            result.append(result[-1] * 2)
            continue
        if result[-1] % 3 == 0 and result[-1] // 3 in numbers:
            result.append(result[-1] // 3)
            continue
        break

    if len(result) == n:
        return result
    return []


n = int(input())
numbers = list(map(int, input().split()))
sequence = find_sequence(n, numbers)
if sequence:
    print(*sequence)