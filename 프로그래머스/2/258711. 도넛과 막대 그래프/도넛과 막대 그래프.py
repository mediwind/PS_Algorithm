from collections import defaultdict


def counting(edges):
    edges_cnt = defaultdict(list)
    for a, b in edges:
        if not a in edges_cnt:
            edges_cnt[a] = [0, 0]
        if not b in edges_cnt:
            edges_cnt[b] = [0, 0]
        
        edges_cnt[a][1] += 1
        edges_cnt[b][0] += 1
    
    return edges_cnt


def solution(edges):
    answer = [0, 0, 0, 0] # 정점, 도넛, 막대, 8자
    tmp = counting(edges)
    # print(tmp)
    
    for k, v in tmp.items():
        if v[0] == 0 and v[1] >= 2: # 정점
            answer[0] = k
        elif v[0] >= 1 and v[1] == 0: # 막대
            # 1번 케이스의 3번 노드와 2번 케이스의 2번 노드와 같은 경우 때문에 v[0] == 1이 아닌 v[0] >= 1
            answer[2] += 1
        elif v[0] >= 2 and v[1] == 2: # 8자
            # 2번 케이스의 11번 노드와 같은 경우 때문에 v[0] == 2가 아닌 v[0] >= 2
            answer[3] += 1
        
    answer[1] = tmp[answer[0]][1] - answer[2] - answer[3]            
    
    return answer