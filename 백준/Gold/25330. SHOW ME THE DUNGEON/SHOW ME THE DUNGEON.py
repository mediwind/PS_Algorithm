def solve_dungeon(remaining_hp, saved_people, accumulated_attack, visited_mask):
    global max_saved_people
    
    max_saved_people = max(max_saved_people, saved_people)

    for i in range(n):
        if not (visited_mask & (1 << i)):
            
            damage_this_turn = accumulated_attack + attacks[i]
            
            if remaining_hp >= damage_this_turn:
                next_hp = remaining_hp - damage_this_turn
                next_mask = visited_mask | (1 << i)

                if memo[next_mask] >= next_hp:
                    continue
                
                memo[next_mask] = next_hp
                
                solve_dungeon(
                    next_hp,
                    saved_people + populations[i],
                    accumulated_attack + attacks[i],
                    next_mask
                )

n, k = map(int, input().split())
attacks = list(map(int, input().split()))
populations = list(map(int, input().split()))

memo = [-1] * (1 << n)
max_saved_people = 0

solve_dungeon(k, 0, 0, 0)

print(max_saved_people)