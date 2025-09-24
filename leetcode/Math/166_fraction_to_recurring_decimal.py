# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    fraction = []
    if (numerator < 0) or (denominator < 0):
        fraction.append("-")
    
    dividend = abs(numerator)
    divisor = abs(denominator)
    fraction.append(str(dividend//divisor))
    remainder = dividend % divisor
    if remainder == 0:
        return "".join(fraction)
    fraction.append(".")
    map_dict ={}
    while remainder != 0:
        print(fraction)
        print(remainder)
        print(map_dict)
        if remainder in map_dict:
            fraction.insert(map_dict[remainder], "(")
            fraction.append(")")
            break
        map_dict[remainder] = len(fraction)
        remainder *= 10
        fraction.append(str(remainder//divisor))
        remainder %= divisor
    return "".join(fraction)

numerator = 4
denominator = 333
print(fractionToDecimal(numerator, denominator))