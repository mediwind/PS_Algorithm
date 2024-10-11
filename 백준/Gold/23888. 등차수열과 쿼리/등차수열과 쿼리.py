import sys
input = sys.stdin.readline


def greatest_common_divisor(x, y):
    if y == 0:
        return x
    while x % y != 0:
        x, y = y, x % y
    return y


first_term, common_difference = map(int, input().split())
num_queries = int(input())

for _ in range(num_queries):
    query_type, left, right = map(int, input().split())

    if query_type == 1:
        sum_right = (right * ((2 * first_term) + (right - 1) * common_difference)) // 2
        sum_left = ((left - 1) * ((2 * first_term) + (left - 2) * common_difference)) // 2
        print(sum_right - sum_left)

    elif query_type == 2:
        if left == right:
            print(first_term + (left - 1) * common_difference)
        else:
            print(greatest_common_divisor(first_term, common_difference))