import itertools

agenda = [input() for _ in range(7)]
d, h = map(int, input().split())

all_days = list(range(7))
max_prob = 0.0

# d개부터 7개까지의 모든 날짜 조합을 생성
for d_prime in range(d, 8):
    for chosen_days_tuple in itertools.combinations(all_days, d_prime):
        chosen_days = list(chosen_days_tuple)

        # 선택된 날짜 조합 내에서 시간별 가용성 계산
        hour_availability = [0] * 24
        for hour_idx in range(24):
            for day_idx in chosen_days:
                if agenda[day_idx][hour_idx] == '.':
                    hour_availability[hour_idx] += 1

        # 가용성을 기준으로 시간 인덱스 정렬
        sorted_hours_indices = sorted(range(24), key=lambda j: hour_availability[j], reverse=True)

        # h개부터 24개까지 시간 조합을 만들어 확률 계산
        for h_prime in range(h, 25):
            chosen_hours = sorted_hours_indices[:h_prime]

            # 선택된 조합 내에서 유효한(비어있는) 슬롯 수 계산
            # 이 값은 이미 hour_availability의 합과 동일함
            available_slots = sum(hour_availability[hour_idx] for hour_idx in chosen_hours)

            # 확률 계산 및 최댓값 갱신
            current_prob = available_slots / (d_prime * h_prime)
            if current_prob > max_prob:
                max_prob = current_prob

print(f"{max_prob:.15f}")