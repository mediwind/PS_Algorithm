def check(cnt):
    for key in ["A", "C", "G", "T"]:
        if cnt.get(key, 0) < minimal[key]:
            return False
    return True


S, P = map(int, input().split())
DNA = input()
acgt = list(map(int, input().split()))
minimal = {"A": acgt[0], "C": acgt[1], "G": acgt[2], "T": acgt[3]}

lt = 0
cnt = dict()
ans = 0
for rt in range(S):
    if rt - lt >= P:
        cnt[DNA[lt]] = cnt.get(DNA[lt], 0) - 1
        lt += 1

    char = DNA[rt]
    cnt[char] = cnt.get(char, 0) + 1
    
    if rt - lt == P - 1:
        if check(cnt):
            ans += 1

print(ans)