import sys
import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    nums = list(map(int, data[1:]))
    
    nums.sort()
    
    diffs = [nums[i] - nums[i - 1] for i in range(1, N)]
    
    result = diffs[0]
    for diff in diffs[1:]:
        result = gcd(result, diff)
    
    print(result)


if __name__ == "__main__":
    main()