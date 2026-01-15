import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

stack = []

for x in A:
    if x >= 0:
        # 양수(0 포함)면 새로운 그룹을 시작할 수 있음 (일단 분리)
        stack.append(x)
    else:
        # 음수면 이전 그룹들에 병합해야 함 (부채 상환)
        curr = x
        
        # 스택에 있는 값들을 하나씩 꺼내서 더함 (합이 0 이상이 될 때까지)
        while stack and curr < 0:
            curr += stack.pop()
        
        # 다 합쳤는데도 음수라면, 이 배열을 구제할 방법이 없음 -> 불가능
        if curr < 0:
            print(-1)
            sys.exit(0)
        
        # 양수가 되었으면 다시 스택에 넣어줌 (하나의 덩어리가 됨)
        stack.append(curr)

# 스택에 남아있는 원소의 개수가 곧 나뉜 부분 배열의 최대 개수
print(len(stack))