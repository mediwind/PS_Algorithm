n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()

result = 1

for i in range(n - 1, -1, -1):
    count = sum(1 for b in b_list if b >= a_list[i])
    result *= (count - (n - 1 - i))

print(result)