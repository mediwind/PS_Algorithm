import sys
input = sys.stdin.readline

N = int(input())
subjects = [set(list(map(int, input().split()))[1:]) for _ in range(N)]

M = int(input())
students = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

for student in students:
    cnt = 0
    for subject in subjects:
        if subject & student == subject:
            cnt += 1
    print(cnt)