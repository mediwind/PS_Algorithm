import sys
input = sys.stdin.readline


def main():
    n, x, y = map(int, input().rstrip().split())
    books = list()
    for _ in range(n):
        w, h = map(int, input().rstrip().split())
        books.append((w, h))

    H = max(h for w, h in books)
    if H > y:
        print("impossible")
        return

    total_width = sum(w for w, h in books)
    if H == y:
        if total_width <= x:
            print(-1)
        else:
            print("impossible")
        return

    upper_h = y - H
    must_lower = list()
    flexible = list()
    
    for w, h in books:
        if h > upper_h:
            must_lower.append(w)
        else:
            flexible.append(w)

    w_must_lower = sum(must_lower)
    if w_must_lower > x:
        print("impossible")
        return

    remaining_lower = x - w_must_lower
    
    dp = [False] * (remaining_lower + 1)
    dp[0] = True
    
    for w in flexible:
        for i in range(remaining_lower, w - 1, -1):
            if dp[i - w]:
                dp[i] = True
    
    max_lower_flexible = 0
    for i in range(remaining_lower + 1):
        if dp[i]:
            max_lower_flexible = i
    
    w_flexible_total = sum(flexible)
    w_flexible_upper = w_flexible_total - max_lower_flexible
    
    if w_flexible_upper <= x:
        print(H)
    else:
        print("impossible")


if __name__ == "__main__":
    main()