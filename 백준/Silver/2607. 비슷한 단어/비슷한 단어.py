from collections import Counter
import sys
input = sys.stdin.readline

n = int(input().strip())
standard = input().strip()
standard_counter = Counter(standard)

ans = 0
for _ in range(n - 1):
    candidate = input().strip()
    candidate_counter = Counter(candidate)
    
    # 두 카운터의 모든 키(문자)를 대상으로 누락(missing)과 초과(extra)를 계산
    all_chars = set(standard_counter.keys()) | set(candidate_counter.keys())
    missing = 0  # standard에 있어야 하는데 candidate에 부족한 수
    extra = 0    # candidate에만 있는 혹은 standard보다 많은 수
    for ch in all_chars:
        diff = standard_counter.get(ch, 0) - candidate_counter.get(ch, 0)
        if diff > 0:
            missing += diff
        else:
            extra += (-diff)
            
    # 한 번의 연산(문자 추가, 삭제, 또는 대체)은 missing와 extra 모두에서 한 단위씩 보정 가능하므로,
    # 두 값 중 큰 값이 실제 필요한 연산 수가 된다.
    ops = max(missing, extra)
    
    if ops <= 1:
        ans += 1

print(ans)