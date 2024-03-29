import sys
import copy

n=int(input())
arr=list(map(int, input().split()))
# n=10
# arr=[7, 6, 10, 9, 8, 1, 2, 3, 4, 5]
arr.insert(0, 0)

res1=list()
res2=list()

def left(target, n):
    cp_arr=copy.copy(arr)
    cnt=0
#     print(cp_arr)
#     print()
    while target!=n:
        for i in range(target, n):
            if target==cp_arr[target]:
                break
            if cp_arr[i]==target:
#                 print(i, cp_arr[i], target)
                cnt+=1
                cp_arr[target:i+1]=cp_arr[i:target-1:-1]
                res1.append(str(target)+" "+str(i))
#                 print(cp_arr)
        target+=1
    
#     print(cnt, res1)
    if cnt==1:
        print("1 1")
        for rs in res1:
            print(rs)
        return True
    elif cnt==2:
        for rs in res1:
            print(rs)
        return True
    else:
        return False

def right(target, n):
    cp_arr=copy.copy(arr)
    cnt=0
#     print(cp_arr)
#     print()
    while target!=n:
        for i in range(target, 0, -1):
            if target==cp_arr[target]:
                break
            if cp_arr[i]==target:
#                 print(i, cp_arr[i], target)
                cnt+=1
                cp_arr[i:target+1]=cp_arr[target:i-1:-1]
                res2.append(str(i)+" "+str(target))
#                 print(cp_arr)
        target-=1
    
#     print(cnt, res2)
    if cnt==1:
        print("1 1")
        for rs in res2:
            print(rs)
        return True
    elif cnt==2:
        for rs in res2:
            print(rs)
        return True
    else:
        print("1 1")
        print("1 1")
        return False
    
if left(1, n+1):
    sys.exit()
right(n, 1)