import re


def is_slump(s):
    return re.fullmatch(r'^([DE]F+)+G$', s) is not None


def is_slimp(s):
    if len(s) < 2:
        return False
    if len(s) == 2 and s == "AH":
        return True
    if s[0] == 'A' and s[-1] == 'C':
        if s[1] == 'B':
            return is_slimp(s[2:-1])
        else:
            return is_slump(s[1:-1])
    return False


n = int(input())

for _ in range(n):
    s = input().strip()
    last_idx_of_c = s.rfind('C')
    if last_idx_of_c != -1:
        if is_slimp(s[:last_idx_of_c + 1]) and is_slump(s[last_idx_of_c + 1:]):
            print("YES")
        else:
            print("NO")
    else:
        if s.startswith("AH") and is_slump(s[2:]):
            print("YES")
        else:
            print("NO")