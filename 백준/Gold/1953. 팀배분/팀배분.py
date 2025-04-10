from collections import deque
import sys
input = sys.stdin.readline


def DFS(player, blue_team):
    if blue_team:
        blue.append(player)
    else:
        white.append(player)
    
    for i in ban[player]:
        if i in Q:
            Q.remove(i)
            DFS(i, not blue_team)


n = int(input().rstrip())
Q = deque()
blue = list()
white = list()

ban = [list() for _ in range(n + 1)]
for i in range(1, n + 1):
    ban[i] = list(map(int, input().rstrip().split()))[1:]
    Q.append(i)

while Q:
    player = Q.popleft()
    DFS(player, True)

print(len(blue))
print(*sorted(blue))
print(len(white))
print(*sorted(white))