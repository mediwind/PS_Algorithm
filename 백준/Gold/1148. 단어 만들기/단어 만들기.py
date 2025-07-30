import sys
input = sys.stdin.readline

words = list()
while True:
    word = input().rstrip()
    if word == '-':
        break
    
    cnt = [0 for _ in range(26)]
    for w in word:
        cnt[ord(w) - 65] += 1
    words.append((cnt, set(word)))

while True:
    board = input().rstrip()
    if board == '#':
        break
    
    board_cnt = [0 for _ in range(26)]
    for alphabet in board:
        board_cnt[ord(alphabet) - 65] += 1
    
    possible = [0 for _ in range(26)]
    for center in range(26):
        if board_cnt[center] == 0:
            continue
        for word_cnt, word_set in words:
            if chr(center + 65) not in word_set:
                continue
            flag = True
            for alphabet in word_set:
                index = ord(alphabet) - 65
                if word_cnt[index] > board_cnt[index]:
                    flag = False
                    break
            if flag:
                possible[center] += 1
    
    mini = min(possible[i] for i in range(26) if board_cnt[i] > 0)
    maxi = max(possible[i] for i in range(26) if board_cnt[i] > 0)
    
    hardest = ''.join(chr(i + 65) for i in range(26) if board_cnt[i] > 0 and possible[i] == mini)
    easiest = ''.join(chr(i + 65) for i in range(26) if board_cnt[i] > 0 and possible[i] == maxi)
    
    print(f"{hardest} {mini} {easiest} {maxi}")