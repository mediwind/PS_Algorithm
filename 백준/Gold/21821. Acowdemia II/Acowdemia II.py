# 출판물의 수와 저자의 수 입력 받기
K, N = map(int, input().split())

# 저자 이름을 인덱스로 매핑할 딕셔너리
members = {}
names = input().split()
for i in range(N):
    members[names[i]] = i

# 결과를 저장할 2차원 배열 초기화
answer = [['?' for _ in range(N)] for _ in range(N)]
for i in range(N):
    answer[i][i] = 'B'  # 자기 자신은 'B'로 표시

# 각 출판물에 대해 처리
for _ in range(K):
    publication = input().split()

    for x in range(N):
        alphabetical = True
        for y in range(x + 1, N):
            if publication[y - 1] > publication[y]:
                alphabetical = False
            if not alphabetical:
                a = members[publication[x]]
                b = members[publication[y]]
                answer[a][b] = '0'
                answer[b][a] = '1'

# 결과 출력
for row in answer:
    print(''.join(row))