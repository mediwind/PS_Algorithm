def solve():
    import sys
    input = sys.stdin.readline
    T = int(input().strip())
    
    for _ in range(T):
        N = input().strip()
        length = len(N)
        digit_sum = sum(int(ch) for ch in N)
        r = digit_sum % 3
        
        # 경우 1: N 자체가 3의 배수이면(즉, 합성수임)
        if r == 0:
            # N이 3의 배수이므로 3이 약수입니다.
            print("0 3")
            continue

        # 경우 2: 자리수 합의 나머지가 1인 경우 -> '1'을 하나 제거하면 새 수의 자리 합이 0 (mod 3)이 됨
        if r == 1:
            removed = False
            for i, ch in enumerate(N):
                if ch == '1':
                    # 왼쪽에서부터 i번째(1-indexed) 자리 제거
                    print(f"{i+1} 3")
                    removed = True
                    break
            # 만약 '1'을 제거할 수 없다면 N은 모두 '5'로 이루어져 있음
            # 모든 자리가 5인 수는 항상 5로 끝나므로 N 자체가 5의 배수입니다.
            if not removed:
                print("0 5")
            continue

        # 경우 3: 자리수 합의 나머지가 2인 경우 -> '5'를 하나 제거하면 새 수의 자리 합이 0 (mod 3)이 됨
        if r == 2:
            removed = False
            for i, ch in enumerate(N):
                if ch == '5':
                    print(f"{i+1} 3")
                    removed = True
                    break
            # 만약 '5'를 제거할 수 없다면 N은 모두 '1'로 이루어져 있음
            # 모든 자리가 1인 수의 경우, 길이가 짝수이면 11의 배수가 되고,
            # 길이가 홀수이면 아무 한 자리를 제거해 짝수 길이로 만든 후 11의 배수가 되게 할 수 있습니다.
            if not removed:
                if length % 2 == 0:
                    print("0 11")
                else:
                    # 예를 들어 첫 번째 자리를 제거
                    print("1 11")
            continue

if __name__ == "__main__":
    solve()