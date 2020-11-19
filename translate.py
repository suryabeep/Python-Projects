# precondition - number is three digits long
def build_three_digits(number):
    if (number == 0):
        return ""
    output = ""
    names = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7: "seven", 8:"eight", 9:"nine", 10: "ten",
            11:"eleven", 12: "twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 
            18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

    hundreds = (int)(number / 100)
    tens = (int)((number % 100) / 10)
    units = number % 10
    last_two = number % 100
    if hundreds != 0:
        output += names[hundreds] + " hundred "
        if last_two != 0:
            output += "and "

    if tens == 0:
        pass
    elif tens == 1:
        output += names[last_two]
    else:
        output += names[tens*10] + " "

    if tens != 1 and units != 0:
        output += names[units]

    return output

while(True):
    number = input("Input a number: ")
    number = (int)(number)
    billions = (int)(number / 1000000000)
    millions = (int)((number % 1000000000) / 1000000)
    thousands = (int)((number % 1000000) / 1000)
    if billions != 0:
        print(build_three_digits(billions) + " billion, ", end="")
    if millions != 0:
        print(build_three_digits(millions) + " million, ", end="")
    if thousands != 0:
        print(build_three_digits(thousands) + " thousand, ", end="")
    print(build_three_digits(number % 1000))
        