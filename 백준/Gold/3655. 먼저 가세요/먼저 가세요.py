import sys
# input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    s = input().rstrip()

    people = list(s)
    people_cnt = dict()
    last_idx = dict()

    for i in range(n):
        people_cnt[people[i]] = people_cnt.get(people[i], 0) + 1
        last_idx[people[i]] = i

    groups = list()
    for i in range(n):
        groups.append((people[i], last_idx[people[i]]))

    groups.sort(key=lambda x: x[1])

    ans = 0
    i = 0
    while i < n:
        current = groups[i][0]
        group_cnt = people_cnt[current]
        last_group_idx = i + group_cnt - 1

        ans += 5 * (last_idx[current] - last_group_idx) * group_cnt
        i = last_group_idx + 1

    print(ans)