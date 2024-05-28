cows = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle', 'Maggie', 'Henrietta']
milk_amount = {cow: 0 for cow in cows}

N = int(input())
for _ in range(N):
    name, amount = input().split()
    milk_amount[name] += int(amount)

scores = sorted(list(set(milk_amount.values())))
if len(scores) == 1 or sum(v == scores[1] for k, v in milk_amount.items()) >= 2:
    print('Tie')
else:
    for k, v in milk_amount.items():
        if v == scores[1]:
            print(k)