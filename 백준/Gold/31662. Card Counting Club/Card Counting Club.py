import heapq
import sys
# input = sys.stdin.readline

def solve():
    try:
        n, m, p = map(int, input().rstrip().split())
    except (ValueError, EOFError):
        return

    players = []
    for i in range(n):
        line = input().rstrip().split()
        name = line[0]
        cards = [int(x) for x in line[1:]]
        heapq.heapify(cards)
        players.append({'name': name, 'hand': cards, 'id': i})

    counted_out_order = []
    
    while len(counted_out_order) < n:
        turn_candidates = []
        
        for player in players:
            if player['hand']:
                smallest_card_value = player['hand'][0]
                turn_candidates.append((smallest_card_value, player['name'], player['id']))
        
        turn_candidates.sort()
        
        winner_id = turn_candidates[0][2]
        
        for player in players:
            if not player['hand']:
                continue

            if player['id'] == winner_id:
                heapq.heappop(player['hand'])
                if not player['hand']:
                    counted_out_order.append(player['name'])
            else:
                penalized_card = heapq.heappop(player['hand']) + p
                heapq.heappush(player['hand'], penalized_card)

    print(*counted_out_order)

solve()