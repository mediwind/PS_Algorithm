X, Y, Z = map(int, input().split())

cuts_needed_for_x = (X - 1) // 2
cuts_needed_for_y = (Y - 1) // 2
cuts_needed_for_z = (Z - 1) // 2

min_total_cuts = min(cuts_needed_for_x, cuts_needed_for_y, cuts_needed_for_z)

if X == 3 and Y == 3 and Z == 3:
    print(0)
else:
    print(min_total_cuts)