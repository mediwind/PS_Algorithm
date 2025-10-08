import itertools

def evaluate(numbers, ops):
    temp_nums = []
    temp_ops = []
   
    current_num = numbers[0]
    for i in range(len(ops)):
        if ops[i] == '*':
            current_num *= numbers[i+1]
        else:
            temp_nums.append(current_num)
            temp_ops.append(ops[i])
            current_num = numbers[i+1]
    temp_nums.append(current_num)

    if not temp_ops:
        return temp_nums[0]

    result = temp_nums[0]
    for i in range(len(temp_ops)):
        if temp_ops[i] == '+':
            result += temp_nums[i+1]
        elif temp_ops[i] == '-':
            result -= temp_nums[i+1]
   
    return result

def solve():
    digits = input().split()
   
    all_results = set()
    operators = ['+', '-', '*']

    for p in set(itertools.permutations(digits)):
               
        nums4 = [int(d) for d in p]
        for op1 in operators:
            for op2 in operators:
                for op3 in operators:
                    res = evaluate(nums4, [op1, op2, op3])
                    if res >= 0:
                        all_results.add(res)

        nums3_a = [int(p[0]), int(p[1]), int(p[2]+p[3])]
        for op1 in operators:
            for op2 in operators:
                res = evaluate(nums3_a, [op1, op2])
                if res >= 0:
                    all_results.add(res)
       
        nums3_b = [int(p[0]), int(p[1]+p[2]), int(p[3])]
        for op1 in operators:
            for op2 in operators:
                res = evaluate(nums3_b, [op1, op2])
                if res >= 0:
                    all_results.add(res)

        nums3_c = [int(p[0]+p[1]), int(p[2]), int(p[3])]
        for op1 in operators:
            for op2 in operators:
                res = evaluate(nums3_c, [op1, op2])
                if res >= 0:
                    all_results.add(res)

        nums2_a = [int(p[0]), int(p[1]+p[2]+p[3])]
        for op in operators:
            res = evaluate(nums2_a, [op])
            if res >= 0:
                all_results.add(res)

        nums2_b = [int(p[0]+p[1]), int(p[2]+p[3])]
        for op in operators:
            res = evaluate(nums2_b, [op])
            if res >= 0:
                all_results.add(res)

        nums2_c = [int(p[0]+p[1]+p[2]), int(p[3])]
        for op in operators:
            res = evaluate(nums2_c, [op])
            if res >= 0:
                all_results.add(res)

    print(len(all_results))

solve()