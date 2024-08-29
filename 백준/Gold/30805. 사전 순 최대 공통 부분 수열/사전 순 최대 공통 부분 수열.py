# 사용자 정의 비교 함수
# 첫 번째 요소를 내림차순으로, 두 번째 요소를 오름차순으로 정렬
def custom_sort_key(pair):
    return (-pair[0], pair[1])


# 입력 값 읽기
N = int(input())
list_A = list(map(int, input().split()))
M = int(input())
list_B = list(map(int, input().split()))

# 값과 인덱스를 쌍으로 생성
pairs_A = [(list_A[i], i) for i in range(N)]
pairs_B = [(list_B[i], i) for i in range(M)]

# 사용자 정의 비교 함수에 따라 쌍 정렬
pairs_A.sort(key=custom_sort_key)
pairs_B.sort(key=custom_sort_key)

# 포인터와 제한 초기화
index_A, index_B = 0, 0
limit_A, limit_B = 0, 0
common_elements = list()

# 공통 요소 찾기
while index_A < N and index_B < M:
    # 현재 요소의 값이 같은지 확인
    if pairs_A[index_A][0] == pairs_B[index_B][0]:
        # limit_A가 현재 인덱스보다 큰 경우, index_A 증가
        if limit_A > pairs_A[index_A][1]:
            index_A += 1
        # limit_B가 현재 인덱스보다 큰 경우, index_B 증가
        elif limit_B > pairs_B[index_B][1]:
            index_B += 1
        # 공통 요소를 찾은 경우
        else:
            limit_A = pairs_A[index_A][1]
            limit_B = pairs_B[index_B][1]
            common_elements.append(pairs_A[index_A][0])
            index_A += 1
            index_B += 1
    # pairs_A의 현재 값이 더 큰 경우, index_A 증가
    elif pairs_A[index_A][0] > pairs_B[index_B][0]:
        index_A += 1
    # pairs_B의 현재 값이 더 큰 경우, index_B 증가
    else:
        index_B += 1

# 결과 출력
print(len(common_elements))
print(" ".join(map(str, common_elements)))