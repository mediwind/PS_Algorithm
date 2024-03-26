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
        if now[1] + now[2] > following[1]: # 다음 과제가 시작될 때까지 현재 과제를 풀지 못하는 경우
            stack.append([now[0], now[2] - (following[1] - now[1])])
        else: # 현재 과제를 다음 과제가 시작하기 전까지 풀 수 있는 경우
            answer.append(now[0])
            remain_time = following[1] - (now[1] + now[2]) # 현재 과제를 푼 뒤 남은 시간
            # print('now:', now, 'stack:', stack, 'remain_time:', remain_time)
            while stack and remain_time >= stack[-1][1]: # 남은 시간으로 밀린 과제를 '완전히' 해치울 수 있을만큼 해치우기
                remain_time -= stack[-1][1]
                answer.append(stack.pop()[0])
            if stack and remain_time >= 1: # 시간이 남았지만 밀린 과제를 '완전히' 해치우지 못한다면 남은 시간 만큼 밀린 최신과제 소요 시간 차감
                stack[-1][1] -= remain_time
            # print('now:', now, 'stack:', stack, 'remain_time:', remain_time)
    
    stack.append([plans[-1][0], plans[-1][2]])
    # print(stack)
    while stack:
        now = stack.pop()
        answer.append(now[0])
    
    return answer