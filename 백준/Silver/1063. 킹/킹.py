move = {
    "R": [0, 1],
    "L": [0, -1],
    "B": [1, 0],
    "T": [-1, 0],
    "RT": [-1, 1],
    "LT": [-1, -1],
    "RB": [1, 1],
    "LB": [1, -1]
}

king, horse, N = input().split()
N = int(N)

king = [-(int(king[1]) - 8) % 8, ord(king[0]) - 65]
horse = [-(int(horse[1]) - 8) % 8, ord(horse[0]) - 65]

for _ in range(N):
    order = input()
    tmp_king = [king[0] + move[order][0], king[1] + move[order][1]]
    
    # 킹이 보드 밖으로 나갈 경우 continue
    if tmp_king[0] < 0 or tmp_king[0] >= 8 or tmp_king[1] < 0 or tmp_king[1] >= 8:
        continue
    
    # 킹이 갈 자리에 돌이 있는 경우
    if tmp_king == horse:
        tmp_horse = [horse[0] + move[order][0], horse[1] + move[order][1]]
        # 돌을 킹이 갈 방향으로 한칸 더 옮겨도 괜찮은 경우에는 자리 갱신
        if 0 <= tmp_horse[0] < 8 and 0 <= tmp_horse[1] < 8:
            king = tmp_king
            horse = tmp_horse
    # 킹이 갈 자리에 애초에 돌이 없는 경우에도 자리 갱신
    else:
        king = tmp_king

print(chr(65 + king[1]) + str(8 - king[0]))
print(chr(65 + horse[1]) + str(8 - horse[0]))