from itertools import permutations
import sys
input = sys.stdin.readline


def distance_check(arr):
    global sx, sy
    
    distance = 0
    
    for i in range(1, len(arr)):
        x_distance = (arr[i][0] - arr[i - 1][0]) ** 2
        y_distance = (arr[i][1] - arr[i - 1][1]) ** 2
        
        maxi = max(x_distance, y_distance)
        distance += (maxi ** 0.5)
    
    x_distance = (sx - arr[0][0]) ** 2
    y_distance = (sy - arr[0][1]) ** 2
    
    maxi = max(x_distance, y_distance)
    distance += (maxi ** 0.5)
    
    return int(distance)
        

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

to_check = list()
cnt_0 = cnt_1 = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            if board[i][j] == 1:
                if (i % 2) == (j % 2):
                    cnt_0 += 1
                else:
                    cnt_1 += 1
                to_check.append((i, j))
            elif board[i][j] == 2:
                sx, sy = i, j

if ((sx % 2) == (sy % 2)) and cnt_1 > 0:
    print("Shorei")
    sys.exit(0)
elif ((sx % 2) != (sy % 2)) and cnt_0 > 0:
    print("Shorei")
    sys.exit(0)
elif cnt_0 + cnt_1 == 0:
    print("Undertaker")
    print(0)
    sys.exit(0)


ans = float('inf')

for perm in permutations(to_check, len(to_check)):
    distance = distance_check(perm)
    ans = min(ans, distance)

print("Undertaker")
print(ans)