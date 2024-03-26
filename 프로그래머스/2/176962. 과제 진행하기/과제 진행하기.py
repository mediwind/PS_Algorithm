def solution(plans):
    answer = []
    copy = list()
    for plan in plans:
        h, m = map(int, plan[1].split(':'))
        tmp = h*60 + m
        copy.append([plan[0], tmp, int(plan[2])])
    
    plans = copy
    plans.sort(key = lambda x: x[1])
    del copy
    # print(plans)
    
    stack = list()
    for i in range(len(plans) - 1):
        now, following = plans[i], plans[i+1]
        if now[1] + now[2] > following[1]:
            stack.append([now[0], now[2] - (following[1] - now[1])])
        else:
            answer.append(now[0])
            remain_time = following[1] - (now[1] + now[2])
            print('now:', now, 'stack:', stack, 'remain_time:', remain_time)
            while stack and remain_time >= stack[-1][1]:
                remain_time -= stack[-1][1]
                answer.append(stack.pop()[0])
            if stack and remain_time >= 1:
                stack[-1][1] -= remain_time
            # print('now:', now, 'stack:', stack, 'remain_time:', remain_time)
    
    stack.append([plans[-1][0], plans[-1][2]])
    # print(stack)
    while stack:
        now = stack.pop()
        answer.append(now[0])
    
    return answer