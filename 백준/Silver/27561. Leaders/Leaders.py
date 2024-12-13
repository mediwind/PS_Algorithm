N = int(input())
breeds = input()
end_indices = list(map(int, input().split()))
end_indices = [x - 1 for x in end_indices]

last_guernsey, last_holstein, first_guernsey, first_holstein = -1, -1, -1, -1

for i in range(N - 1, -1, -1):
    if breeds[i] == 'G':
        last_guernsey = i
    if breeds[i] == 'H':
        last_holstein = i

for i in range(N):
    if breeds[i] == 'G':
        first_guernsey = i
    if breeds[i] == 'H':
        first_holstein = i

count = 0

if end_indices[last_guernsey] >= first_guernsey:
    for i in range(last_guernsey):
        if i == last_holstein:
            continue
        if breeds[i] == 'H' and end_indices[i] >= last_guernsey:
            count += 1

if end_indices[last_holstein] >= first_holstein:
    for i in range(last_holstein):
        if i == last_guernsey:
            continue
        if breeds[i] == 'G' and end_indices[i] >= last_holstein:
            count += 1

if ((end_indices[last_guernsey] >= first_guernsey or (last_guernsey <= last_holstein and end_indices[last_guernsey] >= last_holstein)) and
    (end_indices[last_holstein] >= first_holstein or (last_holstein <= last_guernsey and end_indices[last_holstein] >= last_guernsey))):
    count += 1

print(count)