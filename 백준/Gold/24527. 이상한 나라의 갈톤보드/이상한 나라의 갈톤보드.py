import sys
input = sys.stdin.readline

H = int(input().strip())
Q, R = map(int, input().strip().split())

diff = [0.0] * (H + 3)

for _ in range(Q):
    node_id, beads = map(int, input().strip().split())

    r = int(((8 * node_id + 1)**0.5 - 1) / 2)

    if r * (r + 1) // 2 < node_id:
        r += 1

    prev_nodes_count = r * (r - 1) // 2
    c = node_id - prev_nodes_count

    L = c

    right_bound = c + (H + 1 - r)

    width = right_bound - L + 1

    prob = beads / width

    diff[L] += prob
    diff[right_bound + 1] -= prob

bins = [0.0] * (H + 2)
current_val = 0.0
for i in range(1, H + 2):
    current_val += diff[i]
    bins[i] = current_val

psum = [0.0] * (H + 2)
current_sum = 0.0
for i in range(1, H + 2):
    current_sum += bins[i]
    psum[i] = current_sum

results = []
for _ in range(R):
    a, b = map(int, input().strip().split())

    ans = psum[b] - psum[a - 1]
    results.append(ans)

for result in results:
    print(result)