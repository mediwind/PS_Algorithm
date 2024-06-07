n = int(input())
s = input()

mn = mx = 0
curIdx = 0
while curIdx < n:
    if s[curIdx] == 'F':
        curIdx += 1
        continue

    nextIdx = curIdx + 1
    while nextIdx < n and s[nextIdx] == 'F':
        nextIdx += 1
    if nextIdx == n:
        break

    num_F = nextIdx - curIdx - 1

    if s[nextIdx] == s[curIdx]:
        # Case 1: Solve something like BFFFFFB
        length = num_F + 2
        # First, solve for mn
        if length % 2 == 0:
            # At best we can have something like BEBEBB
            mn += 1
        else:
            # We can alternate BEBEB
            mn += 0
        # Next, solve for mx
        mx += length - 1
    else:
        # Case 2: Solve something like BFFFFFE
        length = num_F + 2
        # First, solve for mn
        if length % 2 == 0:
            # We can alternate BEBEBE
            mn += 0
        else:
            # At best we have BEBEE
            mn += 1
        # Next, solve for mx
        mx += length - 2

    curIdx = nextIdx

# Special case: beginning / ending F's
num_beginning_F = 0
while num_beginning_F < n and s[num_beginning_F] == 'F':
    num_beginning_F += 1
num_ending_F = 0
while num_ending_F < n and s[n - 1 - num_ending_F] == 'F':
    num_ending_F += 1

if num_beginning_F == n:
    # everything is an F! special case
    mn = 0
    mx = n - 1
else:
    # mn doesn't change, since we can always alternate the beginning /
    # ending properly
    mx += num_beginning_F
    mx += num_ending_F

possible_levels = list()
if num_beginning_F == 0 and num_ending_F == 0:
    # Special case: We can only change in increments of two
    assert (mx - mn) % 2 == 0
    possible_levels = list(range(mn, mx + 1, 2))
else:
    possible_levels = list(range(mn, mx + 1))

print(len(possible_levels))
for i in possible_levels:
    print(i)