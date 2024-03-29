cnt=0

n, k=map(int, input().split())
board=[[0]*n for _ in range(n)]
board[-1]=list(map(int, input().split()))

while True:
    # 1번 작업
    fewest=min(board[-1])
    for i in range(n):
        if board[-1][i]==fewest:
            board[-1][i]+=1

    # 2번 작업
    board[-1][0], board[-2][1]=board[-2][1], board[-1][0]

    # 3번 작업
    h, w=2, 1
    to_bear=n-2
    lu, rd=[n-2, 1], [n-1, 1]
    while True:
        on_air=list()
        for i in range(lu[0], rd[0]+1):
            tmp=list()
            for j in range(lu[1], rd[1]+1):
                tmp.append(board[i][j])
            on_air.append(tmp)

        h, w=len(on_air), len(on_air[0])

        if h<=to_bear:
            on_air=list(map(list, zip(*on_air[::-1])))
            for i in range(lu[0], rd[0]+1):
                for j in range(lu[1], rd[1]+1):
                    board[i][j]=0

            h_o, w_o=len(on_air), len(on_air[0])

            for i in range(n-h_o-1, n-1):
                for j in range(rd[1]+1, rd[1]+w_o+1):
                    board[i][j]=on_air[i-n+h_o+1][j-rd[1]-1]

            to_bear-=w_o
            lu[0]=n-h_o-1
            lu[1]=rd[1]+1
            rd[1]+=w_o
        else:
            break
    
    # 4번 작업
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]

    plan=[[[] for _ in range(n)] for _ in range(n)]

    for i in range(lu[0], n):
        for j in range(lu[1], n):
            plan[i][j]=[0, board[i][j], 0]

    for i in range(lu[0], n):
        for j in range(lu[1], n):
            if board[i][j]:
                x, y=i, j
                for d in range(4):
                    xx=x+dx[d]
                    yy=y+dy[d]
                    if 0<=xx<n and 0<=yy<n:
                        if board[xx][yy] and board[x][y]>board[xx][yy]:
                            d=(board[x][y]-board[xx][yy])//5
                            if d>0:
                                plan[x][y][0]-=d
                                plan[xx][yy][2]+=d

    for i in range(lu[0], n):
        for j in range(lu[1], n):
            board[i][j]=sum(plan[i][j])

    # 5번 작업
    line_up=list()
    for i in range(lu[0], n):
        line_up.append(board[i][lu[1]:rd[1]+1])
    line_up=list(map(list, zip(*line_up[::-1])))
    
    tmp=list()
    for i in line_up:
        tmp+=i
    
    board[-1][0:len(tmp)]=tmp

    tmp=board[-1]
    board=[[0]*n for _ in range(n-1)]
    board.append(tmp)

    # 6번 작업
    half_point=n//2
    tmp_1=tmp[:half_point][::-1]
    tmp_2=tmp[half_point:]
    tmp=list()
    tmp.append(tmp_1)
    tmp.append(tmp_2)

    half_point=n//4
    res1=tmp[0][:half_point]
    res2=tmp[0][half_point:]
    res3=tmp[1][:half_point]
    res4=tmp[1][half_point:]

    tmp=list()
    tmp.append(res3[::-1])
    tmp.append(res1[::-1])
    tmp.append(res2)
    tmp.append(res4)

    # 7번 작업
    h, w=len(tmp), len(tmp[0])
    plan=[[[] for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            plan[i][j]=[0, tmp[i][j], 0]

    for i in range(h):
        for j in range(w):
            if tmp[i][j]:
                x, y=i, j
                for d in range(4):
                    xx=x+dx[d]
                    yy=y+dy[d]
                    if 0<=xx<h and 0<=yy<w:
                        if tmp[xx][yy] and tmp[x][y]>tmp[xx][yy]:
                            d=(tmp[x][y]-tmp[xx][yy])//5
                            if d>0:
                                plan[x][y][0]-=d
                                plan[xx][yy][2]+=d

    for i in range(h):
        for j in range(w):
            tmp[i][j]=sum(plan[i][j])

    tmp=list(map(list, zip(*tmp[::-1])))
    ans=[]
    for i in tmp:
        ans+=i

    # 8번 작업
    cnt+=1

    # 9번 작업
    if max(ans)-min(ans)<=k:
        print(cnt)
        break
    
    board=[[0]*n for _ in range(n)]
    board[-1]=ans