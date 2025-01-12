def get_deepest_level(expression):
    max_level = 0
    level = 0
    for char in expression:
        if char == '(':
            level += 1
            max_level = max(max_level, level)
        elif char == ')':
            level -= 1
    return max_level


def evaluate_expression(expression):
    level = 0
    max_level = get_deepest_level(expression)
    stack = []
    for char in expression:
        if char == '(':
            level += 1
            stack.append(OPEN_BRACKET)
        elif char == 'T':
            stack.append(TRUE)
        elif char == 'F':
            stack.append(FALSE)
        elif char == ')':
            temp = stack.pop()
            while stack[-1] != OPEN_BRACKET:
                if ((max_level - level) & 1) == 0:
                    temp &= stack.pop()
                else:
                    temp |= stack.pop()
            stack.pop()
            level -= 1
            stack.append(temp)
    return stack.pop() == 1


OPEN_BRACKET = 2
TRUE = 1
FALSE = 0

test_case_number = 1
while True:
    expression = input()
    if expression == "()":
        break
    result = evaluate_expression(expression)
    print(f"{test_case_number}. {'true' if result else 'false'}")
    test_case_number += 1