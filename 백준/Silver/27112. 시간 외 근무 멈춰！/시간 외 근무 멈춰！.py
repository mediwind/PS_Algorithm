def main():
    # 작업의 개수를 입력받음
    n = int(input())
    # 각 작업의 마감 기한과 소요 시간을 입력받아 리스트에 저장
    works = [list(map(int, input().split())) for _ in range(n)]

    # 작업들을 마감 기한 기준으로 정렬
    works.sort()

    # 현재 날짜, 평일 근무일, 총 근무일, 추가 근무일(시간 외 근무일) 초기화
    day_count = 0
    weekdays = 0
    total_days = 0
    extra_days = 0

    # 각 작업을 순회하며 처리
    for work in works:
        # 현재 날짜가 작업의 마감 기한에 도달할 때까지 반복
        while day_count < work[0]:
            # 평일(월요일~금요일)인 경우 평일 근무일 증가
            if day_count % 7 < 5:
                weekdays += 1
            # 총 근무일 증가
            total_days += 1
            # 다음 날로 이동
            day_count += 1
        
        # 평일 근무일로 작업을 완료할 수 있는 경우
        if weekdays >= work[1]:
            weekdays -= work[1]
        # 평일 근무일이 부족하지만 추가 근무일(시간 외 근무일)로 작업을 완료할 수 있는 경우
        elif weekdays + total_days >= work[1]:
            temp = work[1] - weekdays
            weekdays = 0
            total_days -= temp
            extra_days += temp
        # 추가 근무일을 사용해도 작업을 완료할 수 없는 경우
        else:
            print(-1)
            return

    # 모든 작업을 완료하기 위해 필요한 최소 추가 근무일 출력
    print(extra_days)

if __name__ == "__main__":
    main()