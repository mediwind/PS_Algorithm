N = int(input())
arr = list(map(int, input().split()))
divisors = list()
for i in range(1, int(N ** 0.5) + 1):
    if not N % i:
        divisors.append(i)
        if i * i != N and i != 1:
            divisors.append(N // i)
divisors.sort()

for div in divisors:
    possible = True
    first_seg = arr[0:div]
    target = min(first_seg) + max(first_seg)
    for i in range(div, N, div):
        curr_seg = arr[i:i + div]
        if min(curr_seg) + max(curr_seg) != target:
            possible = False
            break
    
    if possible:
        print(1)
        break
else:
    print(0)