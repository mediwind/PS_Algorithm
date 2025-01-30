from collections import Counter

def count_permutations_in_string(W: str, S: str) -> int:
    g = len(W)
    n = len(S)
    
    if g > n:
        return 0
    
    # 문자열 W의 각 문자의 빈도 계산
    w_count = Counter(W)
    
    # 문자열 S의 처음 g 길이의 부분 문자열의 문자의 빈도 계산
    s_count = Counter(S[:g])
    
    count = 0
    if s_count == w_count:
        count += 1
    
    # 슬라이딩 윈도우 이동
    for i in range(g, n):
        start_char = S[i - g]
        new_char = S[i]
        
        # 윈도우에서 빠지는 문자
        s_count[start_char] -= 1
        if s_count[start_char] == 0:
            del s_count[start_char]
        
        # 윈도우에 새로 추가되는 문자
        s_count[new_char] += 1
        
        # 현재 윈도우의 문자의 빈도가 문자열 W의 문자의 빈도와 동일한지 비교
        if s_count == w_count:
            count += 1
    
    return count

# 입력 받기
g, n = map(int, input().split())
W = input().strip()
S = input().strip()

# 결과 출력
print(count_permutations_in_string(W, S))