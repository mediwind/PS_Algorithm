import heapq

def solve():
    n = int(input().strip())
    masses = list(map(int, input().split()))
    masses.sort()
    target = max(masses)
    cur = 2
    if cur >= target:
        print(0)
        return

    idx = 0
    heap = list()
    steps = 0
    while cur < target:
        while idx < n and masses[idx] < cur:
            heapq.heappush(heap, -masses[idx])
            idx += 1
        if not heap:
            print("NIE")
            return
        largest = -heapq.heappop(heap)
        cur += largest
        steps += 1

    print(steps)

if __name__ == "__main__":
    solve()