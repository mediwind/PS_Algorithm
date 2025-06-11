import sys
input = sys.stdin.readline


def find_next_node(p, q):
    # q == 1: 맨 오른쪽 끝, 다음 레벨 맨 왼쪽
    if q == 1:
        return 1, p + 1
    # p < q: 왼쪽 자식, 부모의 오른쪽 자식이 다음
    elif p < q:
        return q, q - p
    else:
        # 1. 위로 올라가며 처음으로 왼쪽 자식이었던 조상 찾기
        up_p, up_q = p, q
        up_count = 0
        while up_p > up_q:
            up_p, up_q = up_p - up_q, up_q
            up_count += 1
        # 2. 그 조상의 부모의 오른쪽 자식으로 이동
        parent_p, parent_q = up_p, up_q - up_p
        right_child_p, right_child_q = parent_p + parent_q, parent_q
        # 3. 올라온 횟수만큼 왼쪽 자식 방향으로 내려가기
        down_p, down_q = right_child_p, right_child_q
        for _ in range(up_count):
            down_p, down_q = down_p, down_p + down_q
        return down_p, down_q


T = int(input().rstrip())
for t in range(1, T + 1):
    node = input().rstrip().split()[1]
    p, q = map(int, node.split('/'))
    lt, rt = find_next_node(p, q)
    print(f"{t} {lt}/{rt}")