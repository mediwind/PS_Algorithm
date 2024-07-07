import sys

def classify(N, ids):
    count = [0] * 1000001
    for id in ids:
        count[id] += 1
    ans = [0] * (N + 1)
    for c in count:
        if c != 0:
            ans[c] += 1
    return ans

def main():
    input = sys.stdin.read  # Read all input at once
    data = input().split()  # Split by whitespace to get all numbers in a list
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        
        cornell_ids = list(map(int, data[index:index + N]))
        index += N
        
        white_ids = list(map(int, data[index:index + N]))
        index += N
        
        cornell = classify(N, cornell_ids)
        white = classify(N, white_ids)
        
        if cornell == white:
            results.append("what a lovely party")
        else:
            results.append("you've messed up, Cornell")
    
    # Output all results at once to avoid multiple IO operations
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
