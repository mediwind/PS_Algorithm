import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    
    sg = {int(input()): 1 for _ in range(n)}
    sy = {int(input()): 1 for _ in range(m)}
    
    common = set(sg.keys()) & set(sy.keys())
    print(len(common))