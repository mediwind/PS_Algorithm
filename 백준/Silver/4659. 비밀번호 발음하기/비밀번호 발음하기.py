def is_vowel(char):
    return char in 'aeiou'


def check_password(password):
    acceptable_message = "> is acceptable."
    not_acceptable_message = "> is not acceptable."
    
    prev_char = '.'
    count = 0
    has_vowel = False
    
    for char in password:
        if is_vowel(char):
            has_vowel = True
        
        if is_vowel(char) != is_vowel(prev_char):
            count = 1
        else:
            count += 1
        
        if count > 2 or (prev_char == char and char not in 'eo'):
            has_vowel = False
            break
        
        prev_char = char
    
    if has_vowel:
        return f"<{password}{acceptable_message}"
    else:
        return f"<{password}{not_acceptable_message}"


passwords = list()
while True:
    password = input()
    if password == "end":
        break
    passwords.append(password)
    res = check_password(password)
    print(res)