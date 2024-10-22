inputs = [input() for _ in range(3)]

for idx, value in enumerate(inputs):
    if value.isdigit():
        number = int(value)
        position = idx
        break

result = number + 3 - position

if result % 15 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)