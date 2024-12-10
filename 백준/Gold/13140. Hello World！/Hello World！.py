from itertools import permutations

n = int(input())

for perm in permutations(range(10), 7):
    h, e, l, o, w, r, d = perm
    line_1 = (h * 10000) + (e * 1000) + (l * 100) + (l * 10) + o
    line_2 = (w * 10000) + (o * 1000) + (r * 100) + (l * 10) + d
    if h == 0 or w == 0:
        continue
    if line_1 + line_2 == n:
        max_length = max(len(str(line_1)), len(str(line_2)), len(str(n)))
        print(f"  {line_1}")
        print(f"+ {line_2}")
        print("-------")
        if n >= 100000:
            print(f" {n}")
        else:
            print(f"  {n}")
        break
else:
    print("No Answer")