import sys
input = sys.stdin.readline

# 1. 입력 처리
n_str = input().strip()
if n_str:
    n = int(n_str)
    a = list(map(int, input().split()))

    L = max(a)
    C = a.count(L)

    # 최대 자릿수를 요구하는 사람이 단 1명뿐이면 전체 합 1.0을 만드는 것이 불가능
    if C == 1:
        print("NO")
    else:
        R = -1
        # 나머지(Remainder) 케이크를 몰아받을 타겟 R 설정 (최대 자릿수 L을 가진 사람 중 마지막 사람)
        for i in range(n - 1, -1, -1):
            if a[i] == L:
                R = i
                break
        
        # 0이 되는 예외 처리를 위해 사용할 또 다른 최대 자릿수 요구자의 인덱스
        first_L_idx = -1
        for i in range(n):
            if a[i] == L and i != R:
                first_L_idx = i
                break
        
        # 각 자릿수(1 ~ L)별로 지급할 최소 단위(1)의 개수를 누적
        count = [0] * (L + 1)
        for i in range(n):
            if i != R:
                count[a[i]] += 1
                
        # 최대 자릿수 요구자 수의 끝자리가 1인 경우, 0 방지를 위해 1명에게 '2'를 지급
        adjust_idx = -1
        if C % 10 == 1:
            count[L] += 1
            adjust_idx = first_L_idx
            
        # 2. 큰 수 덧셈 최적화 (Carry 처리)
        digits = [0] * (L + 1)
        for k in range(1, L + 1):
            digits[k] = count[k]
            
        # 뒤에서부터 앞으로 자리 올림(Carry) 전파
        for k in range(L, 0, -1):
            if digits[k] >= 10:
                digits[k-1] += digits[k] // 10
                digits[k] %= 10
                
        # 정수부가 1 이상이 되었다면, 최소 단위만 나누어주었는데도 1.0톤을 초과한 것이므로 불가능
        if digits[0] > 0:
            print("NO")
        else:
            # 3. 1.0톤에서 지금까지 나누어준 양 빼기 (나머지 R의 몫 계산)
            w_R_digits = [0] * (L + 1)
            borrow = 0
            for k in range(L, 0, -1):
                val = 0 - digits[k] - borrow
                if val < 0:
                    val += 10
                    borrow = 1
                else:
                    borrow = 0
                w_R_digits[k] = val
                
            w_R_str = "0." + "".join(map(str, w_R_digits[1:]))
            
            # 4. 정답 출력
            print("YES")
            for i in range(n):
                if i == R:
                    # 나머지 케이크 몰아주기
                    print(w_R_str)
                elif i == adjust_idx:
                    # 예외 처리를 위해 '2'를 받은 사람
                    print("0." + "0" * (a[i] - 1) + "2")
                else:
                    # 그 외 모든 사람에게 최소 단위 지급
                    print("0." + "0" * (a[i] - 1) + "1")