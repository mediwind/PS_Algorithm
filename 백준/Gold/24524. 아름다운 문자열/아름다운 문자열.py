s = input()
t = input()

dy = [0 for _ in range(len(t) + 1)]
dy[0] = float('inf')

t_idx = {val: idx + 1 for idx, val in enumerate(t)}
for i in range(len(s)):
    char = s[i]
    if char in t_idx:
        if dy[t_idx[char] - 1] > dy[t_idx[char]]:
            dy[t_idx[char]] += 1

print(dy[-1])