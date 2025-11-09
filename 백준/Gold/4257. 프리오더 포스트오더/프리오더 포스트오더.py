from collections import deque
import sys
input = sys.stdin.readline


def comb(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res


def solve_case(m, pre, post):
    n = len(pre)
    pos = {ch: i for i, ch in enumerate(post)}
    ans = 1

    def dfs(pl, ql, size):
        nonlocal ans
        if size <= 1:
            return
        idx = pl + 1
        cur_post = ql
        children = 0
        end = pl + size
        while idx < end:
            child_root = pre[idx]
            p = pos[child_root]
            child_size = p - cur_post + 1
            children += 1
            dfs(idx, cur_post, child_size)
            idx += child_size
            cur_post += child_size
        ans *= comb(m, children)

    dfs(0, 0, n)
    return ans


while True:
    line = input().rstrip().strip()
    
    if line == "0":
        break
        
    m, pre, post = line.split()
    m = int(m)
    print(solve_case(m, pre, post))