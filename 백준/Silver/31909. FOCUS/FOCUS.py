def swap_keys(key_number):
    for i in range(7):
        for j in range(i + 1, 8):
            if key_number == 2**i + 2**j:
                keys[i], keys[j] = keys[j], keys[i]
                return


n = int(input())
commands = list(map(int, input().split()))
stop_key = int(input())

keys = list(range(8))

for command in commands:
    swap_keys(command)

print(keys[stop_key])