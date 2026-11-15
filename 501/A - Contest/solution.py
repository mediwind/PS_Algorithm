import sys
input = sys.stdin.readline
 
a, b, c, d = map(int, input().split())
 
misha_score = max(3 * a // 10, a - (a // 250) * c)
vasya_score = max(3 * b // 10, b - (b // 250) * d)
 
if misha_score > vasya_score:
    print("Misha")
elif vasya_score > misha_score:
    print("Vasya")
else:
    print("Tie")