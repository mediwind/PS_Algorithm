from math import gcd
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    evens = [num for num in arr if num % 2 == 0]
    odds = [num for num in arr if num % 2 != 0]
    
    reordered_arr = evens + odds
    
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(reordered_arr[i], 2 * reordered_arr[j]) > 1:
                ans += 1
    
    print(ans)