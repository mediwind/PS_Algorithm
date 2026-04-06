import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

# p[i]는 i번째 틈(i-1번 인덱스와 i번 인덱스 사이)을 중심으로 하는 
# 가장 긴 안티 팰린드롬의 반지름(절반 길이)을 저장합니다.
p = [0] * n
center = 0
right = 0
ans = 0

for i in range(1, n):
    # 현재 탐색하려는 중심 i가 이전에 구한 가장 오른쪽 경계(right) 안에 있다면,
    # 중심(center)을 기준으로 한 대칭점(mirror)의 반경을 가져와 초기값으로 씁니다.
    if i < right:
        mirror = 2 * center - i
        p[i] = min(right - i, p[mirror])
    
    # 중심 i를 기준으로 양옆으로 확장하며 안티 팰린드롬인지 검사합니다.
    # 안티 팰린드롬 조건: 왼쪽 문자와 오른쪽 문자가 서로 달라야 함
    while i - 1 - p[i] >= 0 and i + p[i] < n and s[i - 1 - p[i]] != s[i + p[i]]:
        p[i] += 1
        
    # 탐색을 마친 후 가장 오른쪽 경계가 기존보다 더 우측으로 뻗어나갔다면 갱신합니다.
    if i + p[i] > right:
        center = i
        right = i + p[i]
        
    # 중심 i에서 만들어질 수 있는 안티 팰린드롬 부분 문자열의 개수는 그 반지름의 길이와 동일합니다.
    # (예: 반지름이 3이라면 길이가 2, 4, 6인 안티 팰린드롬 3개가 존재함을 의미)
    ans += p[i]

print(ans)