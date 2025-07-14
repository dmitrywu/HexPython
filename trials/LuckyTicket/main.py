def is_happy_ticket(text):
    text_length = len(text)
    if text_length % 2 != 0:
        return False
    half_length = len(text) / 2
    c = 0
    first_half = 0
    last_half = 0
    while c < half_length:
        first_half += int(text[c])
        last_half += int(text[text_length - 1 - c])
        c += 1
    return first_half == last_half


print(is_happy_ticket("123123"))  # True
print(is_happy_ticket("341800"))  # True
print(is_happy_ticket("42"))  # False
print(is_happy_ticket("12345678"))  # False
