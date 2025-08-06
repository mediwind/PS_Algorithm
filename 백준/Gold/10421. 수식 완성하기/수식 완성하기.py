from itertools import product

# 1) 입력
N = int(input())                  # 줄의 총 개수 N
S = list(map(int, input().split()))  # S1, S2, S3, …, SN
K = int(input())                  # 사용할 수 있는 숫자 개수
allowed = input().split()         # 사용할 수 있는 숫자들 (문자)

# 2) S1, S2, 부분곱 자리수 리스트, 최종곱 자리수
S1, S2 = S[0], S[1]
part_lens = S[2:2 + S2]           # S3, S4, … S2+2
final_len = S[-1]                 # SN

count = 0

# 3) A (피승수) 후보: 길이 S1, 각 자리는 allowed 중에서
for A_digits in product(allowed, repeat=S1):
    A = int(''.join(A_digits))
    # 4) B (승수) 후보: 길이 S2
    for B_digits in product(allowed, repeat=S2):
        B = int(''.join(B_digits))

        # 5) 부분곱 검사: B의 일의자리부터 ...
        ok = True
        for idx, d in enumerate(reversed(B_digits)):
            p = A * int(d)
            ps = str(p)
            # 자리수와 각 자리 숫자가 전부 allowed에 있는지 확인
            if len(ps) != part_lens[idx] or any(ch not in allowed for ch in ps):
                ok = False
                break
        if not ok:
            continue

        # 6) 최종곱 검사
        total = A * B
        ts = str(total)
        if len(ts) != final_len or any(ch not in allowed for ch in ts):
            continue

        # 7) 통과하면 카운트
        count += 1

# 8) 정답 출력
print(count)