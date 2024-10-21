n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

shirt = 0
for s in size:
    if s > 0:
        shirt += (s // t)
        if s % t:
            shirt += 1

pen = [(n // p), (n % p)]

print(shirt)
print(*pen)