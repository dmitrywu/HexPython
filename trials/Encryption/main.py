def encrypt(text):
    text_length = len(text)
    text_out = ""
    for i in range(0, text_length - 1, 2):
        text_out += text[i + 1] + text[i]
    if text_length % 2 != 0:
        text_out += text[text_length - 1]
    return text_out


print(encrypt("move"))  # 'omev'
print(encrypt("attack"))  # 'taatkc'
print(encrypt("go!"))  # 'og!'
