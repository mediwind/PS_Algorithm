import sys
from collections import deque
input=sys.stdin.readline

def Hit():
    for x, y, dr in heater:
        if dr==1:
            dx=[-1, 0, 1]
            dy=[1, 1, 1]
            y=y+1
        elif dr==2:
            dx=[-1, 0, 1]
            dy=[-1, -1, -1]
            y=y-1
        elif dr==3:
            dx=[-1, -1, -1]
            dy=[-1, 0, 1]
            x=x-1
        elif dr==4:
            dx=[1, 1, 1]
            dy=[-1, 0, 1]
            x=x+1
        
        if x<0 or x>=R or y<0 or y>=C:
            continue
        
        Q=deque()
        Q.append((x, y, 5))
        
        ch=[[-1]*C for _ in range(R)]
        ch[x][y]=1
        Degree[x][y]+=5
        
        while Q:
            x, y, degree=Q.popleft()
            
            degree-=1
            if degree<=0:
                break
            
            for d in range(3):
                xx=x+dx[d]
                yy=y+dy[d]
                
                if dr==1:
                    if d==0:
                        if (x, y, 0) in wall or (x-1, y, 1) in wall:
                            continue
                    elif d==1:
                        if (x, y, 1) in wall:
                            continue
                    elif d==2:
                        if (x+1, y, 0) in wall or (x+1, y, 1) in wall:
                            continue
                elif dr==2:
                    if d==0:
                        if (x, y, 0) in wall or (x-1, y-1, 1) in wall:
                            continue
                    elif d==1:
                        if (x, y-1, 1) in wall:
                            continue
                    elif d==2:
                        if (x+1, y, 0) in wall or (x+1, y-1, 1) in wall:
                            continue
                elif dr==3:
                    if d==0:
                        if (x, y-1, 1) in wall or (x, y-1, 0) in wall:
                            continue
                    elif d==1:
                        if (x, y, 0) in wall:
                            continue
                    elif d==2:
                        if (x, y, 1) in wall or (x, y+1, 0) in wall:
                            continue
                else:
                    if d==0:
                        if (x, y-1, 1) in wall or (x+1, y-1, 0) in wall:
                            continue
                    elif d==1:
                        if (x+1, y, 0) in wall:
                            continue
                    elif d==2:
                        if (x, y, 1) in wall or (x+1, y+1, 0) in wall:
                            continue
                
                if 0<=xx<R and 0<=yy<C:
                    if ch[xx][yy]==-1:
                        ch[xx][yy]=1
                        Degree[xx][yy]+=degree
                        Q.append((xx, yy, degree))

def Spread(x, y):
    for d in range(4):
        if d==0:
            if (x, y, 0) in wall:
                continue
        elif d==1:
            if (x, y, 1) in wall:
                continue
        elif d==2:
            if (x+1, y, 0) in wall:
                continue
        else:
            if (x, y-1, 1) in wall:
                continue
        
        xx=x+sdx[d]
        yy=y+sdy[d]
        
        if 0<=xx<R and 0<=yy<C:
            if Degree[x][y]>Degree[xx][yy]:
                diff=(Degree[x][y]-Degree[xx][yy])//4
                next_Degree[x][y][0]-=diff
                next_Degree[xx][yy][1]+=diff

R, C, K=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(R)]

heater=list()
To_check=list()
for i in range(R):
    for j in range(C):
        if 1<=board[i][j]<=4:
            heater.append((i, j, board[i][j]))
        elif board[i][j]==5:
            To_check.append((i, j))

W=int(input())
wall=set()
for _ in range(W):
    x, y, t=map(int, input().split())
    x-=1; y-=1
    wall.add((x, y, t))

Degree=[[0]*C for _ in range(R)]

sdx=[-1, 0, 1, 0]
sdy=[0, 1, 0, -1]

ans=0
while ans<101:
    Hit()

    next_Degree=[[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            next_Degree[i][j]=[Degree[i][j]]+[0]

    for i in range(R):
        for j in range(C):
            Spread(i, j)

    for i in range(R):
        for j in range(C):
            Degree[i][j]=next_Degree[i][j][0]+next_Degree[i][j][1]

    for i in range(C):
        if Degree[0][i]>=1:
            Degree[0][i]-=1
        if Degree[R-1][i]>=1:
            Degree[R-1][i]-=1

    for i in range(1, R-1):
        if Degree[i][0]>=1:
            Degree[i][0]-=1
        if Degree[i][C-1]>=1:
            Degree[i][C-1]-=1

    ans+=1
    
    for x, y in To_check:
        if Degree[x][y]<K:
            break
    else:
        break

if ans>100:
    print(101)
else:
    print(ans)