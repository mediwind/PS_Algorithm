# 0. S(n)은 S(n - 1) + ('m' + 'o'*(n+2)) + S(n - 1)개의 길이로 이루어짐
def DFS(length, mid, n):
    if n <= 3:
        return "moo"[n - 1]
    
    wing = (length - mid) // 2 # 2. 현재 길이의 한쪽 날개의 길이를 구합니다.
    
    # 3. 찾으려는 순서 n이 왼쪽 날개, 오른쪽 날개, 가운데 중 어디에 있는지에 따라 탐색합니다.
    if n <= wing:
        return DFS(wing, mid - 1, n)
    
    if n > wing + mid:
        return DFS(wing, mid - 1, n - wing - mid)
    
    if n - wing == 1:
        return "m"
    else:
        return "o"

n = int(input())
length = 3
level = 0
while length < n: # 1. 탐색에 필요한 전체 길이를 구합니다.
    level += 1
    length = (length * 2) + level + 3

# length
# level

res = DFS(length, level + 3, n)
print(res)