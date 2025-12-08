n, m = map(int, input().split())
directions = input().strip()
capacities = list(map(int, input().split()))

indegree = [0] * n
total_milk = sum(capacities)

for idx, d in enumerate(directions):
    if d == 'L':
        move_idx = idx - 1 if idx != 0 else n - 1
    else:
        move_idx = idx + 1 if idx != n - 1 else 0
    indegree[move_idx] += 1

start_nodes = {}
for i in range(n):
    if indegree[i] == 0:
        start_nodes[i] = 0

for start in list(start_nodes.keys()):
    cow = start
    accum_milk = 0
    while indegree[cow] < 2:
        accum_milk += capacities[cow]
        if directions[cow] == 'L':
            cow = cow - 1 if cow != 0 else n - 1
        else:
            cow = cow + 1 if cow != n - 1 else 0
    start_nodes[start] = accum_milk

lost_milk = 0
for milk in start_nodes.values():
    lost_milk += m if milk >= m else milk

print(total_milk - lost_milk)