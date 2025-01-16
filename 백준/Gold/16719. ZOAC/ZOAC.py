def print_word(char_list):
    for char, is_on in char_list:
        if is_on:
            print(char, end='')
    print()


def solution(start, end, word, char_list):
    min_idx = start

    for i in range(start, end + 1):
        if char_list[min_idx][0] > char_list[i][0]:
            min_idx = i

    char_list[min_idx] = (char_list[min_idx][0], True)
    print_word(char_list)

    if min_idx + 1 <= end:
        solution(min_idx + 1, end, word, char_list)

    if min_idx - 1 >= start:
        solution(start, min_idx - 1, word, char_list)


input_str = input().strip()
char_list = [(char, False) for char in input_str]

solution(0, len(input_str) - 1, input_str, char_list)