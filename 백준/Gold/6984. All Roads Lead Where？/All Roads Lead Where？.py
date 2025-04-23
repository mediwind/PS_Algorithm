from collections import defaultdict
import sys
# input = sys.stdin.readline

# 로마에서 특정 도시까지의 경로를 찾는 함수
def get_path_from_rome(city, parent_map):
    """
    주어진 도시에서 루트(로마)까지의 경로를 추적하고,
    로마에서 시작하여 도시까지 내려오는 경로를 반환합니다.
    """
    path_rev = [] # 도시에서 로마까지의 경로: [도시, 부모(도시), ..., 로마]
    curr = city
    while True: # 루트가 처리될 때까지 반복
        path_rev.append(curr)
        # 현재 도시가 루트인지 (부모가 자기 자신인지)
        # 또는 부모 항목이 없는지 (루트만 해당) 확인합니다.
        if curr not in parent_map or curr == parent_map.get(curr):
            break
        # 부모 도시로 이동합니다.
        curr = parent_map.get(curr)
        # 부모 맵이 잘못된 경우 안전 중단 (발생해서는 안 됨)
        if curr is None:
            break
    # 로마에서 도시까지의 순서로 경로를 뒤집습니다.
    return path_rev[::-1] # [로마, ..., 부모(도시), 도시]


# 도로의 수 (m)와 쿼리의 수 (n)를 읽습니다.
m, n = map(int, input().strip().split())

# 부모 관계 저장: 자식 -> 부모
# 입력 줄에서 먼저 언급된 도시가 부모 (낮은 레벨)입니다.
parent = {}
# 나중에 루트를 식별하기 위해 언급된 모든 도시를 추적합니다.
all_cities = set()

# 도로 네트워크 연결 정보를 읽습니다.
for _ in range(m):
    u, v = input().strip().split()
    # u는 부모 (낮은 레벨), v는 자식 (높은 레벨)
    parent[v] = u
    all_cities.add(u)
    all_cities.add(v)

# 로마를 루트로 표시하기 위해 부모를 자기 자신으로 설정합니다.
# 이는 경로 추적 함수의 종료 조건을 제공합니다.
if "Rome" in all_cities:
    parent["Rome"] = "Rome"
else:
    # 대체: "Rome"이 명시적으로 언급되지 않았지만 루트가 존재하는 경우,
    # 부모 맵에서 자식으로 나타나지 않는 도시를 찾습니다.
    # 문제에 따르면 "Rome"은 항상 나타납니다.
    for city in all_cities:
        if city not in parent:
            parent[city] = city # 이 도시를 루트로 표시
            break

results = [] # 각 쿼리에 대한 출력 문자열을 저장할 리스트
# 각 쿼리를 처리합니다.
for _ in range(n):
    # 쿼리의 시작 도시 (s)와 목표 도시 (t)를 읽습니다.
    s, t = input().strip().split()

    # 로마에서 시작 도시 (s)와 목표 도시 (t)까지의 경로를 가져옵니다.
    path_s = get_path_from_rome(s, parent) # [로마, ..., 부모(s), s]
    path_t = get_path_from_rome(t, parent) # [로마, ..., 부모(t), t]

    # 최소 공통 조상 (LCA)의 인덱스를 찾습니다.
    # LCA는 로마에서 시작하는 두 경로에서 공통된 마지막 도시입니다.
    lca_idx = 0
    # 다음 인덱스가 두 경로 모두에 유효하고
    # 다음 인덱스의 도시가 일치하는 동안 반복합니다.
    while (lca_idx + 1 < len(path_s) and
           lca_idx + 1 < len(path_t) and
           path_s[lca_idx + 1] == path_t[lca_idx + 1]):
        lca_idx += 1
    # 루프 후, lca_idx는 두 경로에서 LCA의 인덱스를 가집니다.

    # 최단 경로 구성: s -> ... -> LCA -> ... -> t

    # 1. s에서 LCA까지의 경로 (LCA 포함):
    #    path_s에서 LCA 인덱스 이후의 세그먼트를 가져옵니다.
    #    s에서 LCA까지의 순서로 뒤집습니다.
    path_from_s_to_lca = path_s[lca_idx:][::-1] # [s, 부모(s), ..., LCA]

    # 2. LCA의 자식에서 t까지의 경로 (LCA 제외):
    #    path_t에서 LCA 다음 요소부터 시작하는 세그먼트를 가져옵니다.
    path_from_lca_to_t = path_t[lca_idx + 1:] # [LCA의_자식, ..., 부모(t), t]

    # 두 부분을 결합하여 전체 최단 경로를 형성합니다.
    shortest_path_nodes = path_from_s_to_lca + path_from_lca_to_t

    # 각 도시 이름의 첫 글자를 가져와 출력 문자열을 생성합니다.
    result_string = "".join(city[0] for city in shortest_path_nodes)
    results.append(result_string)

# 모든 결과를 출력합니다. 각 결과는 새 줄에 출력됩니다.
sys.stdout.write("\n".join(results) + "\n")