def solution(s):
    stack = list()
    for i in s:
        flag = False
        while stack and stack[-1] == i:
            stack.pop()
            flag = True

        if not flag:
            stack.append(i)
    
    if stack:
        return 0
    
    return 1