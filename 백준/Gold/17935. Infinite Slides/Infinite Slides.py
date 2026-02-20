import math

W = float(input().strip())

def dist2(t):
    ax = math.cos(t)
    ay = math.sin(t)
    az = -t

    bw = t - W
    bx = 1 + math.cos(bw)
    by = math.sin(bw)
    bz = -2 * bw

    dx = ax - bx
    dy = ay - by
    dz = az - bz
    return dx * dx + dy * dy + dz * dz

ans = float('inf')

start_t = max(W, 2 * W - 10.0)
end_t = 2 * W + 10.0

pieces = 100
step = (end_t - start_t) / pieces

for i in range(pieces):
    lo = start_t + i * step
    hi = start_t + (i + 1) * step
    
    for _ in range(100):
        m1 = (2 * lo + hi) / 3
        m2 = (lo + 2 * hi) / 3
        
        if dist2(m1) < dist2(m2):
            hi = m2
        else:
            lo = m1
            
    ans = min(ans, dist2((lo + hi) / 2))

print(math.sqrt(ans))