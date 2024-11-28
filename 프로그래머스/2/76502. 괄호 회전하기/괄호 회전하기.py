from collections import deque


def valid(pts):
    _open = {'[', '(', '{'}
    
    stack = list()
    for pt in pts:
        if pt in _open:
            stack.append(pt)
        else:
            if not stack:
                return False
            if pt == ']' and stack[-1] != '[':
                return False
            elif pt == ')' and stack[-1] != '(':
                return False
            elif pt == '}' and stack[-1] != '{':
                return False
            stack.pop()
    
    if stack:
        return False
    
    return True


def solution(s):
    n = len(s)
    Q = deque(s)
    answer = 0
    
    for _ in range(n):
        Q.rotate(-1)
        if valid(Q):
            answer += 1
            
    return answer