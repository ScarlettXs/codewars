def square_digits(num):
    concatenated_number = ""
    number_convert_to_str = str(num)
    for digit in number_convert_to_str:
        number_number = int(digit) ** 2
        concatenated_number += str(number_number)
    return int(concatenated_number)