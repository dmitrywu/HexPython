def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(num):
    for i in range(0, 10):
        num = sum_of_square_digits(num)
        # print(num)
        if num == 1:
            return True
    return False


print(is_happy_number(7))
