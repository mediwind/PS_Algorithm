cow_names = [None, None]
num_of_edges, cow_names[0], cow_names[1] = input().split()
num_of_edges = int(num_of_edges)

edge_map = {}
for _ in range(num_of_edges):
    parent, child = input().split()
    edge_map[child] = parent

# print('cow_names:', cow_names)
# print('edge_map:', edge_map)

ancestor_maps = [{}, {}]
for cow_index in range(2):
    current_node = cow_names[cow_index]
    ancestor_maps[cow_index][cow_names[cow_index]] = 0
    while current_node in edge_map:
        next_node = edge_map[current_node]
        ancestor_maps[cow_index][next_node] = ancestor_maps[cow_index][current_node] + 1
        current_node = next_node

# print('ancestor_maps:', ancestor_maps)

common_ancestor = None
distance_to_common_ancestor_cow0 = float("inf")
distance_to_common_ancestor_cow1 = float("inf")
for ancestor_cow0, distance_cow0 in ancestor_maps[0].items():
    if ancestor_cow0 in ancestor_maps[1]:
        distance_cow1 = ancestor_maps[1][ancestor_cow0]
        if distance_to_common_ancestor_cow0 > distance_cow0 and distance_to_common_ancestor_cow1 > distance_cow1:
            common_ancestor = ancestor_cow0
            distance_to_common_ancestor_cow0 = distance_cow0
            distance_to_common_ancestor_cow1 = distance_cow1

# print('common_ancestor:', common_ancestor)

if common_ancestor is None:
    print("NOT RELATED")
elif common_ancestor == cow_names[0] or common_ancestor == cow_names[1]:
    print(f"{common_ancestor} is the ", end="")
    num_of_greats = distance_to_common_ancestor_cow1 if common_ancestor == cow_names[0] else distance_to_common_ancestor_cow0
    for _ in range(num_of_greats - 2):
        print("great-", end="")
    if num_of_greats > 1:
        print("grand-", end="")
    younger_cow = cow_names[1] if common_ancestor == cow_names[0] else cow_names[0]
    print(f"mother of {younger_cow}")
else:
    if distance_to_common_ancestor_cow0 == 1 or distance_to_common_ancestor_cow1 == 1:
        if distance_to_common_ancestor_cow0 == 1 and distance_to_common_ancestor_cow1 == 1:
            print("SIBLINGS")
        else:
            aunt_is_cow0 = distance_to_common_ancestor_cow0 == 1
            aunt = cow_names[0] if aunt_is_cow0 else cow_names[1]
            print(f"{aunt} is the ", end="")
            for _ in range((distance_to_common_ancestor_cow1 if aunt_is_cow0 else distance_to_common_ancestor_cow0) - 2):
                print("great-", end="")
            younger_cow = cow_names[1] if aunt_is_cow0 else cow_names[0]
            print(f"aunt of {younger_cow}")
    else:
        print("COUSINS")