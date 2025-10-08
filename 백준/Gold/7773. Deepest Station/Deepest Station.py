import math

def solve():
    try:
        x, y, d = map(int, input().split())
    except (ValueError, EOFError):
        return

    D_sq = float(x**2 + y**2)
    d_float = float(d)

    epsilon = 1e-9

    if abs(D_sq - d_float**2) < epsilon:
        print("Single staircase")
        return

    if D_sq > d_float**2:
        print("Impossible")
        return

    D = math.sqrt(D_sq)
   
    z_m = (d_float**2 - D_sq) / (2 * (d_float - D))

    ratio = (d_float - z_m) / D
    x_m = float(x) * ratio
    y_m = float(y) * ratio

    print(f"{x_m:.12f} {y_m:.12f} {z_m:.12f}")

solve()