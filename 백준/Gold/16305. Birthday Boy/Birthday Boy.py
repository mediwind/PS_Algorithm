def main():
    # 입력받은 동료 수
    num_colleagues = int(input())
    # 동료들의 이름과 생일 정보를 저장할 리스트
    colleagues_data = [input().strip() for _ in range(num_colleagues)]
    
    max_gap = 0
    best_day = 0
    best_month = 0
    best_date = 0
    
    # 각 월의 일 수
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cumulative_days = [0] * 25
    for i in range(1, 13):
        cumulative_days[i] = cumulative_days[i-1] + days_in_month[i-1]
    days_in_month[0] = 31
    for i in range(13, 25):
        cumulative_days[i] = cumulative_days[i-1] + days_in_month[i-13]
    
    # 동료들의 생일을 일수로 변환하여 저장할 리스트
    birthday_days = []
    for i in range(num_colleagues):
        _, date = colleagues_data[i].split()
        month, day = map(int, date.split('-'))
        birthday_days.append(cumulative_days[month] + day)
        birthday_days.append(cumulative_days[month + 12] + day)
    
    birthday_days.sort()
    
    # 가장 큰 간격을 찾기 위한 리스트
    max_gap_days = []
    for i in range(1, num_colleagues * 2):
        if birthday_days[i] - birthday_days[i-1] == 0:
            continue
        if max_gap < birthday_days[i] - birthday_days[i-1]:
            max_gap = birthday_days[i] - birthday_days[i-1]
            max_gap_days.clear()
            max_gap_days.append(birthday_days[i] - 1)
        elif max_gap == birthday_days[i] - birthday_days[i-1]:
            max_gap_days.append(birthday_days[i] - 1)
    
    for i in range(len(max_gap_days)):
        if max_gap_days[i] > cumulative_days[10] + 27:
            if max_gap_days[i] == 0:
                max_gap_days[i] = cumulative_days[12] + best_day
            best_day = max_gap_days[i]
            for j in range(1, 25):
                if cumulative_days[j] < best_day:
                    best_month = (j - 1) % 12 + 1
                    best_date = best_day - cumulative_days[j]
            print(f"{best_month:02d}-{best_date:02d}")
            return
    
    if max_gap_days[0] == 0:
        max_gap_days[0] = cumulative_days[12] + best_day
    best_day = max_gap_days[0]
    for j in range(1, 25):
        if cumulative_days[j] < best_day:
            best_month = (j - 1) % 12 + 1
            best_date = best_day - cumulative_days[j]
    print(f"{best_month:02d}-{best_date:02d}")

if __name__ == "__main__":
    main()