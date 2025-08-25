fact = [1 for _ in range(10)]
for i in range(1, 10):
    fact[i] = fact[i-1] * i

def page_number(word):
    used = [False for _ in range(9)]
    rank = 0
    n = 9
    for i, ch in enumerate(word):
        idx = ord(ch) - ord('a')  # 0..8
        # 현재 문자보다 작은 문자들 중 아직 사용되지 않은 수를 센다
        smaller = 0
        for k in range(idx):
            if not used[k]:
                smaller += 1
        rank += smaller * fact[n - 1 - i]
        used[idx] = True
    return rank + 1  # 1-based

try:
    T = int(input().strip())
except:
    T = 0

for _ in range(T):
    s = input().strip()
    # 빈 줄이 들어올 수 있으면 건너뛰기
    while s == "":
        s = input().strip()
    print(page_number(s))