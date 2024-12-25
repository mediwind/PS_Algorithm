n = int(input())
result = 0
start = 1
while start < n:
    end = (n - 1) // ((n - 1) // start)
    result += (end - start + 1) * ((n - 1) // start)
    start = end + 1

print(n + result)