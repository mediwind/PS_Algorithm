import heapq
import sys
input = sys.stdin.readline

def bit_update(bit, size, index, value):
    while index <= size:
        bit[index] += value
        index += index & -index


def bit_query(bit, index):
    s = 0
    while index:
        s += bit[index]
        index -= index & -index
    return s

n = int(input().strip())
price_idx = [0] * n
amounts = [0] * n
side = [''] * n
trade_type = [''] * n

price_values = set()
for i in range(n):
    s_i, t_i, p_i, a_i = input().strip().split()
    side[i] = s_i
    trade_type[i] = t_i
    price_val = int(p_i)
    amt = int(a_i)
    price_idx[i] = price_val
    amounts[i] = amt
    price_values.add(price_val)

unique_prices = sorted(list(price_values))
price_to_index = {}
for idx, pv in enumerate(unique_prices, start=1):
    price_to_index[pv] = idx

for i in range(n):
    price_idx[i] = price_to_index[price_idx[i]]

max_idx = len(unique_prices)

bit_buy = [0] * (max_idx + 1)
bit_sell = [0] * (max_idx + 1)

buy_heap = []
sell_heap = []

matches = []

for i in range(n):
    if side[i][0] == 'b':
        if trade_type[i][0] == 'n' or bit_query(bit_sell, price_idx[i]) >= amounts[i]:
            heapq.heappush(buy_heap, (-price_idx[i], i, amounts[i]))
            bit_update(bit_buy, max_idx, price_idx[i], amounts[i])
    else:
        if trade_type[i][0] == 'n' or (bit_query(bit_buy, max_idx) - bit_query(bit_buy, price_idx[i] - 1)) >= amounts[i]:
            heapq.heappush(sell_heap, (price_idx[i], i, amounts[i]))
            bit_update(bit_sell, max_idx, price_idx[i], amounts[i])

    while buy_heap and sell_heap and -buy_heap[0][0] >= sell_heap[0][0]:
        b_price_neg, b_idx, b_amt = heapq.heappop(buy_heap)
        s_price, s_idx, s_amt = heapq.heappop(sell_heap)
        trade_amt = min(b_amt, s_amt)
        matches.append((s_idx + 1, b_idx + 1, trade_amt))
        bit_update(bit_buy, max_idx, -b_price_neg, -trade_amt)
        bit_update(bit_sell, max_idx, s_price, -trade_amt)
        
        if b_amt > trade_amt:
            heapq.heappush(buy_heap, (b_price_neg, b_idx, b_amt - trade_amt))
        if s_amt > trade_amt:
            heapq.heappush(sell_heap, (s_price, s_idx, s_amt - trade_amt))

print(len(matches))
for a, b, c in matches:
    print(a, b, c)