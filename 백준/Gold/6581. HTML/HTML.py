text = []
while True:
    try:
        line = input()
        text.append(line)
    except EOFError:
        break

text = ' '.join(text)
words = text.split()

line_length = 0
output = []

for word in words:
    if word == "<br>":
        output.append('\n')
        line_length = 0
    elif word == "<hr>":
        if line_length > 0:
            output.append('\n')
        output.append('-' * 80 + '\n')
        line_length = 0
    else:
        word_length = len(word)
        if line_length == 0:
            output.append(word)
            line_length += word_length
        elif line_length + word_length + 1 <= 80:
            output.append(' ' + word)
            line_length += word_length + 1
        else:
            output.append('\n' + word)
            line_length = word_length

print(''.join(output))