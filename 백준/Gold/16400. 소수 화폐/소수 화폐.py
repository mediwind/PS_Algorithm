import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

n = int(input())
prime = list()
mod = 123456789

for i in range(2, n + 1):
    if is_prime(i):
        prime.append(i)

dy = [0 for _ in range(n + 1)]
dy[0] = 1
for p in prime:
    for i in range(p, n+1):
        dy[i] = (dy[i] + dy[i-p])%mod
            
print(dy[n])