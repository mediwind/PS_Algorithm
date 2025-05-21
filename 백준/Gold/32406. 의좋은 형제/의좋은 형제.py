import sys
input = sys.stdin.readline


def max_final_difference(bro_fields, bro2_fields):
    # bro_fields[-1]을 최대로 만든 후, 두 형제의 N번째 논 볏단 차이의 절댓값을 반환.
    n = len(bro_fields)
    bro_last = bro_fields[-1]
    bro2_last = bro2_fields[-1]

    for i in range(n - 2):
        if bro_fields[i] > bro2_fields[i]:
            bro_last += bro_fields[i]
            bro2_last += bro2_fields[i]
        else:
            bro_last += bro2_fields[i]
            bro2_last += bro_fields[i]

    bro_last += bro2_fields[-2]
    bro2_last += bro_fields[-2]

    return abs(bro_last - bro2_last)


n = int(input())
first_brother = list(map(int, input().split()))
second_brother = list(map(int, input().split()))

diff1 = max_final_difference(first_brother, second_brother)
diff2 = max_final_difference(second_brother, first_brother)

print(max(diff1, diff2))