import sys
# input = sys.stdin.readline

MOD = 1000000
MAX = 1000


def solve_case(s):
    n = len(s)
    res = [0 for _ in range(MAX * 2 + 2)]
    res2 = [0 for _ in range(MAX * 2 + 2)]
    zero = MAX
    end = MAX
    res[zero] = 1

    for c in s:
        if c == '(':
            zero -= 1
            res[zero] = 0
        elif c == ')':
            zero += 1
        else:  # c == '.'
            # DP 갱신: res2
            res2[end + 1] = res[end]
            res2[zero] = res[zero + 1] if zero < end else 0
            res2[end] = res[end - 1] if zero < end else 0
            
            for i in range(zero + 1, end):
                res2[i] = (res[i - 1] + res[i + 1]) % MOD
                
            end += 1
            res, res2 = res2, res
            
        if zero > end:
            res[zero] = 0
            break
            
    return res[zero] % MOD


try:
    while True:
        s = input().rstrip()
        if not s:
            break
        print(solve_case(s))
except EOFError:
    pass