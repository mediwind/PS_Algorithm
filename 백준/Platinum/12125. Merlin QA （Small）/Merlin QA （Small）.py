import sys
from itertools import permutations
input = sys.stdin.readline

t_str = input().strip()
if t_str:
    T = int(t_str)
    
    for case_num in range(1, T + 1):
        n, m = map(int, input().split())
        
        spells = []
        total_delta = 0
        
        for _ in range(n):
            # M개의 재료 정보를 입력받음
            row = list(map(int, input().split()))
            spells.append(row)
            # 모든 스펠이 주는 순수익(증감)의 총합은 고정되어 있음
            total_delta += sum(row)
            
        max_v = 0
        
        # M개의 재료에 대한 모든 가능한 '최저점 도달 순서'를 확인 (M! 가지의 순열)
        for perm in permutations(range(m)):
            current_v = 0
            
            for spell in spells:
                # 해당 스펠이 특정 순서 관계의 어느 구간에 배치될 때 가장 유리한지 (가장 큰 기여도를 내는지) 계산
                best_contrib = 0
                current_sum = 0
                
                # 순서의 역순으로 더해가며 최댓값을 찾음 (수학적 치환의 결과)
                for idx in reversed(perm):
                    current_sum += -spell[idx]
                    if current_sum > best_contrib:
                        best_contrib = current_sum
                        
                current_v += best_contrib
                
            # M! 개의 순서 케이스 중 가장 큰 보상을 주는 경우를 저장
            if current_v > max_v:
                max_v = current_v
                
        # 최종 보상 = 기본 순수익 + 최적으로 뽑아먹은 창고 재료의 가치
        ans = total_delta + max_v
        print(f"Case #{case_num}: {ans}")