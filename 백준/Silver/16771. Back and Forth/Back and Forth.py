from collections import Counter


def DFS(L):
    if L == 4:
        sm = 0
        for i in range(4):
            if i % 2:
                sm += res[i]
            else:
                sm -= res[i]
        cases.add(sm)
        return
    
    for choice in list(remain_buckets[L % 2].keys()):  # RuntimeError: dictionary changed size during iteration 방지를 위한 Create a copy of the keys
        if remain_buckets[L % 2][choice] > 0:
            res[L] = choice
            remain_buckets[L % 2][choice] -= 1
            remain_buckets[(L + 1) % 2][choice] = remain_buckets[(L + 1) % 2].get(choice, 0) + 1
            DFS(L + 1)
            remain_buckets[L % 2][choice] += 1
            remain_buckets[(L + 1) % 2][choice] -= 1


first_barn = list(map(int, input().split()))
second_barn = list(map(int, input().split()))

first_bucket = Counter(first_barn)
second_bucket = Counter(second_barn)

remain_buckets = [first_bucket, second_bucket]

res = [0 for _ in range(4)]
cases = set()
DFS(0)
print(len(cases))