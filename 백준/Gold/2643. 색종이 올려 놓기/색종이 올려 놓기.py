n = int(input())
paper = [(1000, 1000)]
ans = 0
for _ in range(n):
    w, h = map(int, input().split())
    paper.append((max(w, h), min(w, h)))

paper.sort(reverse = True)

dy = [[0, paper[i][1]] for i in range(n + 1)]
for i in range(1, n + 1): # 1부터 7까지
    for j in range(i - 1, - 1, -1): # ex) i = 5, 4부터 0까지 역순으로
        if dy[j][1] >= paper[i][1] and dy[j][0] + 1 > dy[i][0]:
            dy[i][0] = dy[j][0] + 1
            ans = max(ans, dy[i][0])

print(ans)