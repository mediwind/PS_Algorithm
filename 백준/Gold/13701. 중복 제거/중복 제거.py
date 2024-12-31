import sys
import os

def read_numbers():
    unstdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=1000000)
    ch = unstdin.read(1)
    while True:
        num = 0
        while not (ch == b'\n' or ch == b'' or (ch >= b'0' and ch <= b'9')):
            ch = unstdin.read(1)
        if ch == b'\n' or ch == b'':
            break
        while ch >= b'0' and ch <= b'9':
            num = num * 10 + int(ch)
            ch = unstdin.read(1)
        yield num

def set_bit(n):
    byte_index = n // 8
    bit_index = n % 8

    is_new = (bit_array[byte_index] & (1 << bit_index)) == 0

    bit_array[byte_index] |= (1 << bit_index)

    return is_new

bit_array = bytearray(4194304)

try:
    sys.stdin = open("13701_input.txt")
except FileNotFoundError:
    pass

for number in read_numbers():
    if set_bit(number):
        print(number, end=" ")
print()