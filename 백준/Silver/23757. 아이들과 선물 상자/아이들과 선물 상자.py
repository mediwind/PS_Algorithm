import heapq as hq

n, m = map(int, input().split())
presents = list(map(int, input().split()))
students = list(map(int, input().split()))

presents = list(map(lambda x: -x, presents))
hq.heapify(presents)
for st in students:
    now = -hq.heappop(presents)
    if now < st:
        print(0)
        break
    hq.heappush(presents, -(now - st))
else:
    print(1)