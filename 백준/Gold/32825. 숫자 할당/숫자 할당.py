# 특정 방정식이 유망한지 (pruning)
def is_promising(equation_name):
    equation = eqs[equation_name]
    current_sum = 0
    unknown_vars = []
    for idx in equation['vars']:
        if var_values[idx] != 0:
            current_sum += var_values[idx]
        else:
            unknown_vars.append(idx)

    # 아직 할당되지 않은 변수에 최소/최대값을 넣어 합의 범위를 계산
    min_sum = current_sum + sum(range(1, len(unknown_vars) + 1))
    max_sum = current_sum + sum(range(14 - len(unknown_vars), 14))

    # 목표 합이 가능한 범위 내에 있는지 확인
    return equation['target'] >= min_sum and equation['target'] <= max_sum


# 특정 변수가 할당될 때, 관련된 모든 방정식이 유망한지 확인
def are_constraints_ok(variable_index):
    relevant_equations = []
    for eq_name, eq in eqs.items():
        if variable_index in eq['vars']:
            relevant_equations.append(eq_name)

    # 관련된 모든 방정식이 유망한지 확인
    for eq_name in relevant_equations:
        if not is_promising(eq_name):
            return False
    return True


# 백트래킹 함수
def find_solutions(var_index):
    global solution_count

    # 모든 변수에 값이 할당되면, 해를 찾음
    if var_index == 13:
        # 모든 방정식이 만족하는지 확인
        for eq_name, eq in eqs.items():
            actual_sum = sum(var_values[i] for i in eq['vars'])
            if actual_sum != eq['target']:
                return  # 하나라도 만족하지 않으면, 해가 아님

        solution_count += 1  # 모든 조건을 만족하면, 해의 개수 증가
        return

    # 다음 변수에 값을 할당
    for num in range(1, 14):
        if not is_num_used[num]:
            var_values[var_index] = num
            is_num_used[num] = True

            # 제약 조건을 만족하는지 확인하고, 재귀 호출
            if are_constraints_ok(var_index):
                find_solutions(var_index + 1)

            # 백트래킹: 할당 해제 및 사용 여부 초기화
            var_values[var_index] = 0
            is_num_used[num] = False


# 입력 받기
a_val, b_val, c_val, d_val, e_val, f_val, g_val, h_val = map(int, input().split())

# 변수 이름과 인덱스 매핑 (a, b, ..., m)
var_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda_sym', 'mu', 'nu']

# 방정식 정의 (이름, 관련 변수 인덱스, 목표 합)
eqs = {
    'eq_A': {'vars': [0, 4, 8, 11], 'target': a_val},  # A = a + e + i + l
    'eq_B': {'vars': [1, 5, 9, 12], 'target': b_val},  # B = b + f + j + m
    'eq_C': {'vars': [2, 6, 10], 'target': c_val},  # C = c + g + k
    'eq_D': {'vars': [3, 7], 'target': d_val},  # D = d + h
    'eq_E': {'vars': [0, 1, 2, 3], 'target': e_val},  # E = a + b + c + d
    'eq_F': {'vars': [4, 5, 6, 7], 'target': f_val},  # F = e + f + g + h
    'eq_G': {'vars': [8, 9, 10], 'target': g_val},  # G = i + j + k
    'eq_H': {'vars': [11, 12], 'target': h_val}   # H = l + m
}

solution_count = 0  # 해의 개수

is_num_used = [False] * 14  # 숫자 1~13 사용 여부
var_values = [0] * 13  # 각 변수에 할당된 값

find_solutions(0)  # 백트래킹 시작
print(solution_count)