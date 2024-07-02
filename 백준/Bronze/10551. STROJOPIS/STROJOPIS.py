fingers = ['1QAZ', '2WSX', '3EDC', '4RFV5TGB', '6YHN7UJM', '8IK,', '9OL.', "0P;/-['=]"]

ans = [0 for _ in range(8)]
string = input()
for s in string:
    for i in range(8):
        if s in fingers[i]:
            ans[i] += 1

for a in ans:
    print(a)