import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    l -= 1  # 0-based index로 변환
    arr = list(map(int, input().split()))
    
    # 구간 [l, r]의 합을 최소화하기 위해 두 가지 경우를 고려.
    
    # 1. [l, r] 구간을 포함하는 배열의 뒷부분을 정렬하여 최소화
    brr = arr[:l] + sorted(arr[l:])
    
    # 2. [l, r] 구간을 포함하는 배열의 앞부분을 정렬하여 최소화
    crr = sorted(arr[:r])[::-1] + arr[r:]
    
    # 두 경우 중 더 작은 값을 선택
    print(min(sum(brr[l:r]), sum(crr[l:r])))