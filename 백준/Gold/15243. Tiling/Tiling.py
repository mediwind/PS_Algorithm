MOD = 1000000007

# --- 행렬 연산 함수 ---

def multiply(A, B, size):
    """두 행렬 A와 B를 곱한 결과를 반환 (MOD로 나눈 나머지 계산 포함)"""
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def identity(size):
    """주어진 크기의 단위 행렬을 반환"""
    I = [[0] * size for _ in range(size)]
    for i in range(size):
        I[i][i] = 1
    return I

def power(A, n, size):
    """행렬 A를 n제곱한 결과를 반환 (이진 거듭제곱법 사용)"""
    res = identity(size)
    base = A
    while n > 0:
        if n % 2 == 1:
            res = multiply(res, base, size)
        base = multiply(base, base, size)
        n //= 2
    return res

# --- 타일링 논리 ---

memo_trans = {}

def find_next_masks(r, prev_mask, next_mask_profile, results):
    """
    재귀적으로 다음 상태 프로파일을 계산
    r: 현재 행 (0부터 2까지)
    prev_mask: 이전 열의 상태 프로파일
    next_mask_profile: 현재 열의 상태 프로파일
    results: 가능한 다음 상태 프로파일을 저장할 리스트
    """
    if r == 3:  # 열의 끝에 도달한 경우
        results.append(next_mask_profile)
        return

    # 이전 열에서 현재 행이 이미 채워진 경우
    if (prev_mask >> r) & 1:
        find_next_masks(r + 1, prev_mask, next_mask_profile, results)
        return

    # 가로 도미노를 놓는 경우
    find_next_masks(r + 1, prev_mask, next_mask_profile | (1 << r), results)

    # 세로 도미노를 놓는 경우
    if r + 1 < 3 and not ((prev_mask >> (r + 1)) & 1):
        find_next_masks(r + 2, prev_mask, next_mask_profile, results)

def get_transitions(prev_mask):
    """
    이전 상태 프로파일에서 가능한 다음 상태 프로파일을 계산하고 캐싱
    """
    if prev_mask in memo_trans:
        return memo_trans[prev_mask]

    results = []
    find_next_masks(0, prev_mask, 0, results)
    memo_trans[prev_mask] = results
    return results


# 입력 받기
W = int(input())

# W가 홀수인 경우, 3xW 영역은 홀수 크기이므로 타일링 불가능
if W % 2 != 0:
    print(0)
else:
    # 상태 전이 행렬 M 생성
    size = 8  # 2^3 = 8개의 상태
    M = [[0] * size for _ in range(size)]
    for k in range(size):  # k는 이전 상태 프로파일
        transitions = get_transitions(k)
        for j in transitions:  # j는 다음 상태 프로파일
            M[j][k] = 1

    # M^W 계산 (행렬 거듭제곱)
    M_pow_W = power(M, W, size)

    # 초기 상태에서 상태 0으로 도달하는 경우의 수 출력
    print(M_pow_W[0][0])