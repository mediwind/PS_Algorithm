import sys
input = sys.stdin.readline

n = int(input().rstrip())

enter = {input().rstrip(): i for i in range(n)}
exit = {input().rstrip(): i for i in range(n)}

ans = 0
exit_list = list(exit.keys())
for i in range(len(exit_list)):
    tmp1 = enter[exit_list[i]]
    for j in range(i + 1, len(exit_list)):
        tmp2 = enter[exit_list[j]]
        if tmp1 > tmp2:
            ans += 1
            break

print(ans)