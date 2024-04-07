from itertools import combinations


def To_sum(arr):
    res = [0 for _ in range(4)]
    price = 0
    for i in arr: # 식재료 번호
        for j in range(4): # 영양 컬럼
            res[j] += board[i][j]
        price += board[i][-1]
    
    return res, price


n = int(input())
m_n = list(map(int, input().split()))
board = {idx:list(map(int, input().split())) for idx in range(1, n + 1)}

answer_price = float('inf')
answer_nutr = list()
for i in range(1, n + 1): # 뽑을 개수
#     print(i)
    for comb in combinations(range(1, n + 1), i): # 1 ~ n 선택지 중에서
#         print(comb)
        res, price = To_sum(comb)
        if res[0] >= m_n[0] and res[1] >= m_n[1] and res[2] >= m_n[2] and res[3] >= m_n[3]:
            if answer_price >= price:
                answer_price = price
                answer_nutr.append((comb, price))
#     print()

if answer_price == float('inf'):
    print(-1)
else:
    print(answer_price)
    answer_nutr.sort(key = lambda x: (x[1], x[0])) # 주의) 사전순으로 [1, 2, 3]이 [3] 보다 앞선다.
    print(*answer_nutr[0][0])