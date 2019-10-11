def intToRoman(num):
    string = ""
    while num > 0:
        if num >= 1000:
            string += "M"
            num -= 1000
        elif num >= 900:
            string += "CM"
            num -= 900
        elif num >= 500:
            string += "D"
            num -= 500
        elif num >= 400:
            string += "CD"
            num -= 400
        elif num >= 100:
            string += "C"
            num -= 100
        elif num >= 90:
            string += "XC"
            num -= 90
        elif num >= 50:
            string += "L"
            num -= 50
        elif num >= 40:
            string += "XL"
            num -= 40
        elif num >= 10:
            string += "X"
            num -= 10
        elif num >= 9:
            string += "IX"
            num -= 9
        elif num >= 5:
            string += "V"
            num -= 5
        elif num >= 4:
            string += "IV"
            num -= 4
        elif num >= 1:
            string += "I"
            num -= 1
    return string


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    def romanValue(c):
        if c == 'I':
            return 1
        if c == 'V':
            return 5
        if c == 'X':
            return 10
        if c == 'L':
            return 50
        if c == 'C':
            return 100
        if c == 'D':
            return 500
        if c == 'M':
            return 1000
        return 0

    num = 0
    length = len(s)
    for index in range(length):
        char = s[index]
        if index < length - 1:
            nextchar = s[index + 1]
            value1 = romanValue(char)
            value2 = romanValue(nextchar)
            if value1 < value2:
                num -= value1
            else:
                num += value1
        else:
            num += romanValue(char)

    return num


print(intToRoman(59))
print(romanToInt("LIX"))