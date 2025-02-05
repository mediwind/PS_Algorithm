def solution(dirs):
    
    directions = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1)
    }
    
    board = [[0 for _ in range(11)] for _ in range(11)]
    ch = set()
    
    x, y = 5, 5
    for d in dirs:
        direction = directions[d]
        
        xx = x + direction[0]
        yy = y + direction[1]
        
        if xx < 0 or xx >= 11 or yy < 0 or yy >= 11:
            continue
        
        if (x, y, xx, yy) not in ch and (xx, yy, x, y) not in ch:
            ch.add((x, y, xx, yy))
        
        x, y = xx, yy
    
    answer = len(ch)
    
    return answer