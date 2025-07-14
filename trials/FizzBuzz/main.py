def fizz_buzz(begin: int, end: int) -> str:
    if end - begin < 0:
        return ""
    out_string = ""
    for i in range(begin, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            out_string += "FizzBuzz"
        elif i % 3 == 0:
            out_string += "Fizz"
        elif i % 5 == 0:
            out_string += "Buzz"
        else:
            out_string += str(i)
        out_string += " "

    return out_string.rstrip()


print(fizz_buzz(1, 5))
# => 1 2 Fizz 4 Buzz
print(fizz_buzz(11, 20))
# => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
print(fizz_buzz(1, 0))
print(fizz_buzz(7, 7))
