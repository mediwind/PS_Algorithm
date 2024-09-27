def main():
    n = int(input())
    
    remainder = 0
    count = 0
    seen_remainders = set()
    
    while True:
        count += 1
        remainder = (remainder * 10 + 1) % n
        if remainder == 0:
            print(count)
            return
        if remainder in seen_remainders:
            break
        seen_remainders.add(remainder)
    
    print(-1)


if __name__ == "__main__":
    main()