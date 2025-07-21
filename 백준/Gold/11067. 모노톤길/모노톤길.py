import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    
    cafes = [tuple(map(int, input().split())) for _ in range(N)]
    cafes.sort()

    ordered_path = list()
    current_x_group = list()

    for cafe in cafes:
        if not current_x_group or cafe[0] == current_x_group[0][0]:
            current_x_group.append(cafe)
        else:
            last_y = ordered_path[-1][1] if ordered_path else 0
            
            if last_y > current_x_group[0][1]:
                current_x_group.reverse()
            
            ordered_path.extend(current_x_group)
            
            current_x_group = [cafe]

    if current_x_group:
        last_y = ordered_path[-1][1] if ordered_path else 0
        if last_y > current_x_group[0][1]:
            current_x_group.reverse()
        ordered_path.extend(current_x_group)

    query = list(map(int, input().split()))
    for k in query[1:]:
        x, y = ordered_path[k - 1]
        print(x, y)