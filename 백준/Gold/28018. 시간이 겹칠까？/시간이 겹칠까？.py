import sys

n = int(input())

enter_counts = [0] * 1000001
exit_counts = [0] * 1000001
active_counts = [0] * 1000001

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    enter_counts[start] += 1
    exit_counts[end] += 1

for i in range(1, 1000001):
    active_counts[i] = active_counts[i - 1] + enter_counts[i] - exit_counts[i - 1]

q_count = int(sys.stdin.readline().rstrip())
queries = [int(x) for x in sys.stdin.readline().split()]

for query in queries:
    print(active_counts[query])