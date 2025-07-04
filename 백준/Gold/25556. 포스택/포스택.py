N = int(input())
nums = list(map(int, input().split()))
stacks = [[float('-inf')] for _ in range(4)]

for num in nums:
    idx = -1
    max_top = float('-inf')
    for i in range(4):
        top = stacks[i][-1]
        if top < num and top > max_top:
            idx = i
            max_top = top
    if idx == -1:
        # 조건에 맞는 곳이 없으면 비어있는 스택에 넣기
        for i in range(4):
            if stacks[i][-1] == float('-inf'):
                stacks[i].append(num)
                break
        else:
            print("NO")
            break
    else:
        stacks[idx].append(num)
else:
    print("YES")