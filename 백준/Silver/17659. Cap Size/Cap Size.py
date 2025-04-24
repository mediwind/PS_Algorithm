import sys

def solve():
    input = sys.stdin.readline
    K = int(input().strip())  # 데이터 세트 수

    results = [] # 각 데이터 세트의 결과를 저장할 리스트

    for ds in range(1, K + 1):
        n, t = map(int, input().split())
        sizes = list(map(int, input().split()))  # 오름차순 정렬된 모자 크기 리스트

        lower_bound = -1      # "too small"(f=1) 피드백 중 가장 큰 크기
        upper_bound = 1001    # "too large"(f=-1) 피드백 중 가장 작은 크기
        perfect_fits = set()  # "perfect fit"(f=0) 피드백을 받은 크기들의 집합
        inconsistent = False

        # 피드백 처리
        for _ in range(t):
            c, f = map(int, input().split())

            if f == 0:
                # 완벽히 맞음 피드백
                perfect_fits.add(c)
            elif f == 1:
                # too small → 실제 크기는 c보다 커야 함
                lower_bound = max(lower_bound, c)
            else:  # f == -1
                # too large → 실제 크기는 c보다 작아야 함
                upper_bound = min(upper_bound, c)

        # 모순 검사
        # 1. 두 개 이상의 다른 크기가 완벽하게 맞는다고 보고된 경우
        if len(perfect_fits) > 1:
            inconsistent = True

        # 2. "too small"의 최대 크기가 "too large"의 최소 크기보다 크거나 같은 경우
        if lower_bound >= upper_bound:
            inconsistent = True

        # 3. 완벽하게 맞는 크기가 하나 보고되었지만, 다른 피드백과 모순되는 경우
        exact_fit = -1
        if len(perfect_fits) == 1:
            exact_fit = list(perfect_fits)[0]
            # 완벽하게 맞는 크기가 lower_bound보다 작거나 같거나, upper_bound보다 크거나 같으면 모순
            if not (lower_bound < exact_fit < upper_bound):
                inconsistent = True

        # 결과 계산 및 저장
        current_result = []
        current_result.append(f"Data Set {ds}:")
        if inconsistent:
            current_result.append("Inconsistent feedback")
        else:
            if exact_fit != -1:
                # 완벽하게 맞는 크기가 하나 있고 모순이 없는 경우
                current_result.append("1")
            else:
                # 완벽하게 맞는 크기가 보고되지 않았고 모순이 없는 경우
                # 가능한 후보 개수 계산 (lower_bound < size < upper_bound)
                cnt = 0
                for s in sizes:
                    if lower_bound < s < upper_bound:
                        cnt += 1
                current_result.append(str(cnt))

        results.append("\n".join(current_result))

    # 전체 결과 출력 (데이터 세트 사이에 빈 줄 포함)
    print("\n\n".join(results))


if __name__ == "__main__":
    solve()