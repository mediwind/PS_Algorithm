def finding():
    if c in arr:
        return True
        
    lt, rt = 0, n - 1
    while lt < rt:
        total = arr[lt] + arr[rt]
        if total == c:
            return True
        elif total > c:
            rt -= 1
        else:
            diff = c - total
            if arr[lt] != diff and arr[rt] != diff and binary_search(lt, rt, diff):
                return True
            lt += 1


def binary_search(lt, rt, diff):
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid] < diff:
            lt = mid + 1
        elif arr[mid] > diff:
            rt = mid - 1
        else:
            return True
    
    return False

n, c = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if finding():
    print(1)
else:
    print(0)