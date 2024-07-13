def high_and_low(numbers):
    highest_number = ""
    lowest_number = ""
    for number in numbers.split(" "):
        integer = int(number)
        if highest_number == "":
            highest_number = integer
        elif highest_number != "" :
            if highest_number > integer:
                highest_number = highest_number
            else:
                highest_number = integer
        
        if lowest_number == "":
            lowest_number = integer
        elif lowest_number != integer:
            if lowest_number <integer:
                lowest_number = lowest_number
            else:
                lowest_number = integer
    return str(highest_number) +" "+ str(lowest_number)