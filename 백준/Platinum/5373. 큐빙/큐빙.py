def rotate(order):
    global up, down, front, back, left, right
    o1, o2=order[0], order[1]
    if o1=='F':
        if o2=='-':
            front=list(map(list, zip(*front[::-1])))
            up[0], left[2], down[2], right[2]=right[2][::-1], up[0][::-1], left[2], down[2]
        else:
            front=list(map(list, zip(*front)))[::-1]
            up[0], left[2], down[2], right[2]=left[2][::-1], down[2], right[2], up[0][::-1]
    
    elif o1=='B':
        if o2=='-':
            back=list(map(list, zip(*back[::-1])))
            up[2], right[0], down[0], left[0]=left[0][::-1], up[2][::-1], right[0], down[0]
        else:
            back=list(map(list, zip(*back)))[::-1]
            up[2], right[0], down[0], left[0]=right[0][::-1], down[0], left[0], up[2][::-1]
    
    elif o1=='U':
        left=list(map(list, zip(*left)))
        right=list(map(list, zip(*right)))
        
        if o2=='-':
            up=list(map(list, zip(*up[::-1])))
            back[0], left[0], front[2], right[2]=right[2], back[0][::-1], left[0], front[2][::-1]
        else:
            up=list(map(list, zip(*up)))[::-1]
            back[0], left[0], front[2], right[2]=left[0][::-1], front[2], right[2][::-1], back[0]
        
        left=list(map(list, zip(*left)))
        right=list(map(list, zip(*right)))
    
    elif o1=='D':
        left=list(map(list, zip(*left)))
        right=list(map(list, zip(*right)))
        
        if o2=='-':
            down=list(map(list, zip(*down[::-1])))
            back[2], left[2], front[0], right[0]=left[2][::-1], front[0], right[0][::-1], back[2]
        else:
            down=list(map(list, zip(*down)))[::-1]
            back[2], left[2], front[0], right[0]=right[0], back[2][::-1], left[2], front[0][::-1]
        
        left=list(map(list, zip(*left)))
        right=list(map(list, zip(*right)))
    
    elif o1=='L':
        front=list(map(list, zip(*front)))
        back=list(map(list, zip(*back)))
        up=list(map(list, zip(*up)))
        down=list(map(list, zip(*down)))
        
        if o2=='-':
            left=list(map(list, zip(*left[::-1])))
            back[0], down[0], front[0], up[0]=up[0], back[0], down[0], front[0]
        else:
            left=list(map(list, zip(*left)))[::-1]
            back[0], down[0], front[0], up[0]=down[0], front[0], up[0], back[0]
        
        front=list(map(list, zip(*front)))
        back=list(map(list, zip(*back)))
        up=list(map(list, zip(*up)))
        down=list(map(list, zip(*down)))
    
    elif o1=='R':
        front=list(map(list, zip(*front)))
        back=list(map(list, zip(*back)))
        up=list(map(list, zip(*up)))
        down=list(map(list, zip(*down)))
        
        if o2=='-':
            right=list(map(list, zip(*right[::-1])))
            back[2], down[2], front[2], up[2]=down[2], front[2], up[2], back[2]
        else:
            right=list(map(list, zip(*right)))[::-1]
            back[2], down[2], front[2], up[2]=up[2], back[2], down[2], front[2]
        
        front=list(map(list, zip(*front)))
        back=list(map(list, zip(*back)))
        up=list(map(list, zip(*up)))
        down=list(map(list, zip(*down)))

t=int(input())
for _ in range(t):
    up=[['w' for _ in range(3)] for _ in range(3)]
    down=[['y' for _ in range(3)] for _ in range(3)]
    front=[['r' for _ in range(3)] for _ in range(3)]
    back=[['o' for _ in range(3)] for _ in range(3)]
    left=[['g' for _ in range(3)] for _ in range(3)]
    right=[['b' for _ in range(3)] for _ in range(3)]
    n=int(input())
    order_list=list(input().split())
    for i in order_list:
        rotate(i)
    print(''.join(up[2]))
    print(''.join(up[1]))
    print(''.join(up[0]))