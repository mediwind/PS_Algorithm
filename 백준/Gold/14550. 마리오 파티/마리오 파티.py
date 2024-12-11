def calculate_max_score(num_positions, max_dice_roll, num_turns, coins):
    previous_scores = list([float("-inf")] * (num_positions + 2))
    previous_scores[0] = 0
    max_score = float("-inf")

    while num_turns > 0:
        num_turns -= 1
        current_scores = list([float("-inf")] * (num_positions + 2))

        for i in range(1, num_positions + 2):
            for gap in range(1, max_dice_roll + 1):
                if i - gap < 0 or previous_scores[i - gap] == float("-inf"):
                    continue
                current_scores[i] = max(current_scores[i], previous_scores[i - gap] + coins[i])

        max_score = max(max_score, current_scores[num_positions + 1])
        previous_scores = current_scores

    return max_score

data = list()
while True:
    try:
        line = input()
        if line.strip() == '':
            break
        data.append(line)
    except EOFError:
        break

index = 0
results = list()

while True:
    board = list(map(int, data[index].split()))
    index += 1
    
    if board == list([0]):
        break
    
    num_positions, max_dice_roll, num_turns = board
    
    coins = list()
    while len(coins) < num_positions:
        coins.extend(list(map(int, data[index].split())))
        index += 1
    coins = list([0]) + coins + list([0])

    results.append(calculate_max_score(num_positions, max_dice_roll, num_turns, coins))

for result in results:
    print(result)