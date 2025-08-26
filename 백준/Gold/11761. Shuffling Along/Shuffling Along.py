from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


def build_permutation(n, mode):
    """
    한 번의 퍼펙트 셔플(모드: "in" 또는 "out")이 만들어내는
    old_index -> new_index 순열을 반환.
    """
    # 인덱스 리스트로 반으로 나눔
    if mode == "out":
        # out: 앞쪽(첫 절반)이 같거나 1 더 많음(홀수일 때)
        k = (n + 1) // 2  # 앞쪽 길이
        first = list(range(0, k))
        second = list(range(k, n))
        # interleave starting with first
        new_order = []
        i = j = 0
        while i < len(first) or j < len(second):
            if i < len(first):
                new_order.append(first[i]); i += 1
            if j < len(second):
                new_order.append(second[j]); j += 1
    else:
        # in: 뒤쪽(두번째 절반)이 같거나 1 더 많음(홀수일 때)
        k = n // 2  # 앞쪽 길이 (작음 when odd)
        first = list(range(0, k))
        second = list(range(k, n))
        # interleave starting with second
        new_order = []
        i = j = 0
        while i < len(first) or j < len(second):
            if j < len(second):
                new_order.append(second[j]); j += 1
            if i < len(first):
                new_order.append(first[i]); i += 1

    # old_index -> new_index 매핑 생성
    perm = [0] * n
    for new_idx, old_idx in enumerate(new_order):
        perm[old_idx] = new_idx
    return perm


def permutation_order(perm):
    """
    순열 perm (perm[i] = 이미지) 의 순서를 계산 (모든 사이클 길이의 LCM).
    """
    n = len(perm)
    seen = [False] * n
    res = 1
    for i in range(n):
        if not seen[i]:
            # 사이클 추적
            cur = i
            length = 0
            while not seen[cur]:
                seen[cur] = True
                cur = perm[cur]
                length += 1
            if length > 0:
                res = lcm(res, length)
    return res


parts = input().strip().split()
n = int(parts[0])
mode = parts[1].lower()  # 'in' 또는 'out'
perm = build_permutation(n, mode)
ans = permutation_order(perm)
print(ans)