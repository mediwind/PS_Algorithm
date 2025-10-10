import sys
input = sys.stdin.readline

raw_input = input().rstrip()
scores = []
for char in raw_input:
    if '1' <= char <= '9':
        scores.append(int(char))
    elif char == 'S':
        scores.append(10)
    elif char == '-':
        scores.append(0)
    elif char == 'P':
        scores.append(10 - scores[-1])

total_score = 0
throw_index = 0
for frame in range(10):
    if throw_index >= len(scores):
        break

    if scores[throw_index] == 10:
        total_score += 10 + scores[throw_index + 1] + scores[throw_index + 2]
        throw_index += 1
    elif scores[throw_index] + scores[throw_index + 1] == 10:
        total_score += 10 + scores[throw_index + 2]
        throw_index += 2
    else:
        total_score += scores[throw_index] + scores[throw_index + 1]
        throw_index += 2

print(total_score)