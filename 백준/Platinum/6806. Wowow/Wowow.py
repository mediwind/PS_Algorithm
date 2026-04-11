import sys
input = sys.stdin.readline

N = int(input())

queries = []
ratings = set()

for _ in range(N):
    line = input().split()
    queries.append(line)
    
    if line[0] in ('N', 'M'):
        ratings.add(int(line[2]))

# 좌표 압축
sorted_ratings = sorted(ratings)
compress = {v: i for i, v in enumerate(sorted_ratings)}
rev = {i: v for i, v in enumerate(sorted_ratings)}

size = len(sorted_ratings)

# 세그트리
tree = [0] * (4 * size)

def update(node, start, end, idx, val):
    if start == end:
        tree[node] += val
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(node*2, start, mid, idx, val)
    else:
        update(node*2+1, mid+1, end, idx, val)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(node, start, end, k):
    if start == end:
        return start
    
    mid = (start + end) // 2
    
    # 오른쪽 subtree 먼저 (큰 값)
    if tree[node*2+1] >= k:
        return query(node*2+1, mid+1, end, k)
    else:
        return query(node*2, start, mid, k - tree[node*2+1])

id_to_rating = {}
rating_to_id = {}

output = []

for q in queries:
    if q[0] == 'N':
        x = int(q[1])
        r = int(q[2])
        
        id_to_rating[x] = r
        rating_to_id[r] = x
        
        idx = compress[r]
        update(1, 0, size-1, idx, 1)
        
    elif q[0] == 'M':
        x = int(q[1])
        new_r = int(q[2])
        
        old_r = id_to_rating[x]
        
        # 제거
        update(1, 0, size-1, compress[old_r], -1)
        
        # 추가
        id_to_rating[x] = new_r
        rating_to_id[new_r] = x
        update(1, 0, size-1, compress[new_r], 1)
        
    else:  # Q
        k = int(q[1])
        
        idx = query(1, 0, size-1, k)
        rating = rev[idx]
        
        output.append(str(rating_to_id[rating]))

print('\n'.join(output))