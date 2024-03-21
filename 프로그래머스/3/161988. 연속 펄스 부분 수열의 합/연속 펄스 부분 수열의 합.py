from sys import maxsize


def solution(sequence):
    n = len(sequence)
    
    # 각각 1로 시작하는, -1로 시작하는 펄스 수열로 연속 펄스 부분 수열 2개 생성
    arr_1 = list()
    arr_2 = list()
    one = 1
    for i in sequence:
        arr_1.append(i * one)
        arr_2.append(i * -one)
        one *= -1
    
    # 만들어진 2개의 연속 펄스 부분 수열들의 누적합 생성
    sum_1 = [arr_1[0]] + [0 for _ in range(n)] 
    sum_2 = [arr_2[0]] + [0 for _ in range(n)]
    for i in range(1, len(sequence)):
        sum_1[i] = sum_1[i-1] + arr_1[i]
        sum_2[i] = sum_2[i-1] + arr_2[i]
    
    answer = -maxsize # 프로그래머스는 float('-inf') 비지원
    # mini_1과 mini_2는 현재까지의 누적합 중 가장 작은 값
    # mini_1과 mini_2는 늘 0이하 이므로 mini_x을 현재까지의 연속 펄스 부분 수열의 합인 sx에서 빼주면 sx에서 나올 수 있는 최대 연속 펄스 부분 수열의 합이 나온다
    mini_1, mini_2 = 0, 0
    for i in range(n):
        # s1과 s2는 시작부터 현재까지의 '총' 누적합
        s1 = sum_1[i]
        s2 = sum_2[i]
        
        answer = max(answer, s1 - mini_1, s2 - mini_2)
        
        mini_1 = min(mini_1, s1)
        mini_2 = min(mini_2, s2)
    
    return answer