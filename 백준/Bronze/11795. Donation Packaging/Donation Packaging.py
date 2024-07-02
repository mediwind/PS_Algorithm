setA, setB, setC = 0, 0, 0

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    setA += a
    setB += b
    setC += c

    packages = min(setA, setB, setC)
    if packages < 30:
        print("NO")
    else:
        print(packages)
        setA -= packages
        setB -= packages
        setC -= packages