import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input().rstrip())
words = {input().rstrip() for _ in range(N)}

len_s = len(S)

# dy[i]는 S의 첫 i개 문자가 A의 단어들로 만들어질 수 있는지를 나타냄
dy = [0 for _ in range(len_s + 1)]
dy[0] = True # 빈 문자열은 항상 만들 수 있다고 가정 (기저 사례)

for i in range(1, len_s + 1):
    for j in range(i):
        if dy[j]:
            substring = S[j:i]
            if substring in words:
                dy[i] = True
                break # dy[i]가 True가 되는 경우를 찾았으므로 더 이상 j를 탐색할 필요 없음
        
if dy[len_s]:
    print(1)
else:
    print(0)