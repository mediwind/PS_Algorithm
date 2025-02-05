def valid_k(k, lines):
    depth = 0
    i_val = None  # 들여쓰기 단위 i (양의 정수)
    for line in lines:
        # line의 앞부분에는 's'와 't'만 있고 마지막 문자는 '{' 또는 '}'
        # 실제 indent 값:
        count_spaces = line.count('s')
        count_tabs = line.count('t')
        actual = count_spaces + k * count_tabs
        
        if line[-1] == '{':
            expected = depth  # expected indent = depth * i_val, i_val 아직 미정
            # 깊이가 0이면 실제도 0이어야 함.
            if depth == 0:
                if actual != 0:
                    return False
            else:
                # depth > 0일 때, i_val 결정 또는 검증
                if actual % depth != 0:
                    return False
                curr_i = actual // depth
                if curr_i <= 0:
                    return False
                if i_val is None:
                    i_val = curr_i
                elif i_val != curr_i:
                    return False
            depth += 1
        
        elif line[-1] == '}':
            depth -= 1
            expected = depth  # expected indent = depth * i_val
            if depth == 0:
                if actual != 0:
                    return False
            else:
                if actual % depth != 0:
                    return False
                curr_i = actual // depth
                if curr_i <= 0:
                    return False
                if i_val is None:
                    i_val = curr_i
                elif i_val != curr_i:
                    return False
        else:
            # 문제 조건상 마지막 문자는 항상 '{' 혹은 '}'임.
            return False
    return True


n = int(input())
lines = [input().strip() for _ in range(n)]

ans = -1
for k in range(1, 1001):
    if valid_k(k, lines):
        ans = k
        break
print(ans)