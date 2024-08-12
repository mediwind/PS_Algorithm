LIMIT = 1440
DAYS = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def main():
    times = [input().strip() for _ in range(4)]
    s1 = get_min(times[0])
    s2 = get_min(times[1])
    f1 = get_min(times[2])
    f2 = get_min(times[3])
    solution(s1, s2, f1, f2)

    
def solution(s1, s2, f1, f2):
    for i in range(LIMIT):
        cur = s1 + f1 * i
        if cur - s2 < 0 or (cur - s2) % f2 != 0:
            continue

        min = cur % 60
        cur //= 60
        hour = cur % 24
        cur //= 24

        print(DAYS[cur % 7])
        print(f"{lpad(hour)}:{lpad(min)}")
        return
    print("Never")

    
def lpad(num):
    return f"{num:02}"


def get_min(hhmm):
    hh, mm = map(int, hhmm.split(":"))
    return hh * 60 + mm


if __name__ == "__main__":
    main()