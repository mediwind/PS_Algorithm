def find_sequence(N, L):
    while L <= 100:
        constant = sum(range(L))
        first_num = (N - constant) / L

        if first_num.is_integer() and first_num >= 0:
            sequence = [int(first_num) + i for i in range(L)]
            return sequence
        else:
            L += 1

    return [-1]


N, L = map(int, input().split())
result = find_sequence(N, L)
print(" ".join(map(str, result)))