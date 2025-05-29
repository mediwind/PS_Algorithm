import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
hierarchy_cows_input = list(map(int, input().split()))

fixed_positions_input = list()
for _ in range(K):
    c, p = map(int, input().split())
    fixed_positions_input.append((c, p))

# 소 1이 착유될 수 있는 가장 빠른 위치를 찾기 위해 1부터 N까지 시도
for pos_cow1_trial in range(1, N + 1):
    # 각 시도마다 새로운 착유 순서 배열을 만듦 (0은 빈 자리)
    milking_order = [0 for _ in range(N + 1)] # 1-indexed
    possible_this_trial = True

    # 1. 소 1의 시험 위치가 다른 소의 고정 위치와 충돌하는지 확인
    for fc, fp in fixed_positions_input:
        if fc != 1 and fp == pos_cow1_trial:
            possible_this_trial = False
            break
    if not possible_this_trial:
        continue

    # 2. 소 1의 시험 위치가 소 1 자신의 고정 위치와 충돌하는지 확인
    cow1_fixed_pos = -1
    for fc, fp in fixed_positions_input:
        if fc == 1:
            cow1_fixed_pos = fp
            break
    if cow1_fixed_pos != -1 and cow1_fixed_pos != pos_cow1_trial:
        possible_this_trial = False
        continue

    # 소 1을 시험 위치에 배치
    milking_order[pos_cow1_trial] = 1

    # 3. 다른 소들의 고정 위치 배치 및 충돌 확인
    for fc, fp in fixed_positions_input:
        if fc == 1: # 소 1은 이미 처리됨
            continue
        if milking_order[fp] == 0:
            milking_order[fp] = fc
        elif milking_order[fp] != fc: # 해당 위치에 다른 소가 이미 있거나, 고정된 소가 다름
            possible_this_trial = False
            break
    if not possible_this_trial:
        continue

    # 4. 계층 구조 소들 배치
    last_placed_hierarchy_cow_actual_pos = 0 # 계층 소가 마지막으로 배치된 실제 위치 (1-indexed)

    for h_cow in hierarchy_cows_input:
        # 계층 소가 이미 배치되어 있는지 확인 (고정 위치 또는 소 1)
        is_h_cow_placed = False
        current_pos_of_h_cow = 0
        for i in range(1, N + 1):
            if milking_order[i] == h_cow:
                is_h_cow_placed = True
                current_pos_of_h_cow = i
                break

        if is_h_cow_placed:
            if current_pos_of_h_cow < last_placed_hierarchy_cow_actual_pos:
                # 계층 순서 위반 (이미 배치된 소가 이전 계층 소보다 앞에 있음)
                possible_this_trial = False
                break
            last_placed_hierarchy_cow_actual_pos = current_pos_of_h_cow
        else:
            # 계층 소를 빈 자리에 배치해야 함
            found_spot_for_h_cow = False
            for p in range(last_placed_hierarchy_cow_actual_pos + 1, N + 1):
                if milking_order[p] == 0: # 빈 자리 발견
                    milking_order[p] = h_cow
                    last_placed_hierarchy_cow_actual_pos = p
                    found_spot_for_h_cow = True
                    break
            if not found_spot_for_h_cow:
                # 이 계층 소를 배치할 적절한 빈 자리가 없음
                possible_this_trial = False
                break

    if possible_this_trial:
        print(pos_cow1_trial)
        break