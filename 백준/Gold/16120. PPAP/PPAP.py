# 1. P 하나를 PPAP로 바꿀 수 있다.
# 2. 스택의 끝부분 4자리가 PPAP라면 P만 남도록 pop() 3회 실시
# 3. 이 과정을 끝냈을 때 스택에 P만 남는다면 PPAP 문자열이 맞다.
s = input()
stack = list()

for i in s:
    stack.append(i)
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()

if stack == ['P']:
    print("PPAP")
else:
    print("NP")
