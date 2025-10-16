n, seed, leverage = map(int, input().split())
prices = list(map(int, input().split()))
best = seed

def dfs(day, wallet, owe):
    global best
    
    if wallet > best:
        best = wallet
    wallet -= owe
    
    if day == n - 1:
        return
    dfs(day + 1, wallet, 0)
    loan = wallet * leverage
    
    if wallet + loan < prices[day]:
        return
    total_cash = wallet + loan
    shares = total_cash // prices[day]
    
    if shares == 0:
        return
    
    for sell in range(day + 1, n):
        new_wallet = total_cash + (prices[sell] - prices[day]) * shares
        dfs(sell, new_wallet, loan)

dfs(0, seed, 0)
print(best)