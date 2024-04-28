n = int(input())
trees = list(map(int, input().split()))
h = sum(trees)
d = h // 3
if h % 3:
    print("NO")
else:
    cnt = 0
    for t in trees:
        cnt += (t // 2)
    if cnt < d:
        print("NO")
    else:
        print("YES")