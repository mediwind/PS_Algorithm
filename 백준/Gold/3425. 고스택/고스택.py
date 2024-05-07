import sys
input = sys.stdin.readline


def execution(orders, num):
    stack = [num]
    for order in orders:
        if order[:3] == "NUM":
            n = int(order[4:])
            stack.append(n)
        elif not stack:
            return "ERROR"
        elif order == "POP":
            stack.pop()
        elif order == "INV":
            stack[-1] *= -1
        elif order == "DUP":
            stack.append(stack[-1])
        elif len(stack) == 1:
            return "ERROR"
        elif order == "SWP":
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif order == "ADD":
            temp = stack.pop() + stack.pop()
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stack.append(temp)
        elif order == "SUB":
            temp = -stack.pop() + stack.pop()
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stack.append(temp)
        elif order == "MUL":
            temp = stack.pop() * stack.pop()
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stack.append(temp)
        elif order == "DIV":
            a, b = stack.pop(), stack.pop()
            if a == 0:
                return "ERROR"
            temp = abs(b) // abs(a)
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                temp = -temp
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stack.append(temp)
        elif order == "MOD":
            a, b = stack.pop(), stack.pop()
            if a == 0:
                return "ERROR"
            temp = abs(b) % abs(a)
            if b < 0:
                temp = -temp
            if abs(temp) > 10 ** 9:
                return "ERROR"
            stack.append(temp)
        else:
            return "ERROR"

    if len(stack) == 1:
        return stack[0]
    return 'ERROR'


while True:
    orders = []
    while True:
        order = input().strip()
        if order == "QUIT":
            quit()
        if order == "END":
            break
        orders.append(order)

    n = int(input())
    for _ in range(n):
        num = int(input())
        print(execution(orders, num))
    print()
    input()