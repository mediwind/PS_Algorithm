import sys
input = sys.stdin.readline


def calculate_operations(string_a, string_b):
    len_a = len(string_a)
    len_b = len(string_b)

    if len_a != len_b:
        print("-1")
        return

    operations = 0
    index_a = 0
    index_b = 0

    while True:
        while index_a < len_a and string_a[index_a] == 'a':
            index_a += 1
        while index_b < len_b and string_b[index_b] == 'a':
            index_b += 1
        if index_a >= len_a or index_b >= len_b:
            break
        operations += abs(index_a - index_b)
        index_a += 1
        index_b += 1

    print(operations)


T = int(input())
for _ in range(T):
    string_a, string_b = input().strip().split()
    calculate_operations(string_a, string_b)