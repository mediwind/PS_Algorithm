def perfect_square_number(number):
    number = int(number) # math.floor와 int는 동작 방식이 다름에 주의
    return int(number ** 0.5)**2 == number # 루트를 씌우고 int로 소수점을 모두 버린 뒤 제곱을 해도 기존과 같다면 True

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

answer = -1
for i in range(n):
    for j in range(m):
#         print('시작 좌표:', [i, j], board[i][j])
        for rd in range(-n, n): # 등차가 음인 경우도 있어야 역방향 숫자도 읽을 수 있다.
            for cd in range(-m, m): # -n + 1 혹은 -m + 1로 해두면 n과 m이 1일때 에러
#                 print('행의 등차:', rd, '열의 등차:', cd)
                number = ''
                x, y = i, j
                if rd == 0 and cd == 0: # 등차가 모두 0인 경우 while이 무한 loop를 돌게되며, 어차피 시작 좌표 하나만 해당되므로 continue
                    continue
                while 0 <= x < n and 0 <= y < m:
                    number += board[x][y]
                    if perfect_square_number(number): # 완전제곱수 판별 함수를 while안에 넣어야 다른 숫자들 사이에 둘러싸인 완전제곱수도 탐색 가능
                        answer = max(answer, int(number))
#                         print('number:', number)
                    x += rd
                    y += cd
#         print()

print(answer)