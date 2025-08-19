def min_ops_to_unify(s):
    # map colors to 0,1,2
    mp = {'R':0, 'G':1, 'B':2}
    n = len(s)
    arr = [mp[ch] for ch in s]

    INF = 10**18
    best = INF

    for target in range(3):
        cur = arr[:]  # 복사
        ops = 0
        # i는 연산 시작 인덱스(0-based)
        for i in range(n - 2):
            # i 위치를 target으로 만들기 위해 필요한 연산 횟수 (0..2)
            need = (target - cur[i]) % 3
            if need:
                ops += need
                # need번 연산을 i, i+1, i+2에 더함 (mod 3)
                cur[i] = (cur[i] + need) % 3
                cur[i+1] = (cur[i+1] + need) % 3
                cur[i+2] = (cur[i+2] + need) % 3
        # 마지막 두가 target인지 확인
        if cur[n-2] == target and cur[n-1] == target:
            if ops < best:
                best = ops

    return best if best != INF else -1


n = int(input().strip())
s = input().strip()
print(min_ops_to_unify(s))