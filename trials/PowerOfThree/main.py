def is_power_of_three(three):
    if three < 2:
        return False
    while three % 3 == 0:
        three = three / 3
    return 1 == three


print(is_power_of_three(3))  # True
print(is_power_of_three(2))  # False
print(is_power_of_three(9))  # True
