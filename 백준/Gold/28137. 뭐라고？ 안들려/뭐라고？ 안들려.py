import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    points = defaultdict(int)
    
    index = 2
    for _ in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points[y - k * x] += 1
    
    cnt = 0
    for value in points.values():
        cnt += value * (value - 1)
    
    print(cnt)

if __name__ == "__main__":
    main()