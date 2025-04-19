import sys
input = sys.stdin.readline


def get_depth(node):
    cnt = 0
    square = 0
    while True:
        cnt += (k ** square)
        if cnt >= node:
            return square
        square += 1


def get_parent(node):
    return (node - 2) // k + 1


n, k, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    
    if k == 1:
        # k가 1인 경우, 트리는 선형 구조이므로 거리 계산은 절대값 차이
        print(abs(x - y))
        continue

    # 두 노드의 깊이를 계산
    depth_x = get_depth(x)
    depth_y = get_depth(y)
    distance = 0

    # 두 노드의 깊이를 맞추기 위해 더 깊은 노드를 위로 이동
    while depth_x > depth_y:
        x = get_parent(x)
        depth_x -= 1
        distance += 1
    while depth_y > depth_x:
        y = get_parent(y)
        depth_y -= 1
        distance += 1

    # 두 노드가 같은 조상이 될 때까지 위로 이동
    while x != y:
        x = get_parent(x)
        y = get_parent(y)
        distance += 2

    print(distance)