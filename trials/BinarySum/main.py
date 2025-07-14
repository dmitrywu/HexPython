def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(num):
    print(sum_of_square_digits(num))
    return


print(is_happy_number(7))
