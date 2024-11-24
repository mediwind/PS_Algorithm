def solution(s):
    change_count = 0
    deleted_zeros = 0

    while s != '1':
        decimal_number = 0
        for i in s:
            if i == '0':
                deleted_zeros += 1
            else:
                decimal_number += 1

        s = bin(decimal_number)[2:]
        change_count += 1

    return [change_count, deleted_zeros]