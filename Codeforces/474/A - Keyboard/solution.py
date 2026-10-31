import sys
input = sys.stdin.readline
 
shift_dir = input().strip()
typed = input().strip()
 
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
 
offset = -1 if shift_dir == 'R' else 1
 
result = []
for ch in typed:
    idx = keyboard.index(ch)
    result.append(keyboard[idx + offset])
 
print("".join(result))