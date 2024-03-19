from collections import defaultdict


def solution(arrows):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    sx, sy = 0, 0
    ch = defaultdict(list)
    
    for arrow in arrows:
        for d in range(2):
            xx = sx + dx[arrow]
            yy = sy + dy[arrow]
            if not (xx, yy) in ch:
                ch[(sx, sy)].append((xx, yy))
                ch[(xx, yy)].append((sx, sy))
            elif (xx, yy) in ch and (sx, sy) not in ch[(xx, yy)]:
                answer += 1
                ch[(sx, sy)].append((xx, yy))
                ch[(xx, yy)].append((sx, sy))
            
            sx = xx
            sy = yy
    
    # for k, v in ch.items():
    #     print(k, v)
    return answer