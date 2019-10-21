import sys


def reverse(x):
    negative = x < 0
    if negative:
        x *= -1
    y = 0
    while x != 0:
        digit = x % 10
        x = int(x / 10)

        # prevent overflow by returning 0 if number too large
        if y > sys.maxsize / 10:
            return 0
        if y == sys.maxsize / 10 and digit > 7:
            return 0

        # otherwise proceed
        y = y * 10 + digit
    if negative:
        y *= -1
    return y


# TEST CASE
number = 257289529
print(number, " -> ", reverse(number))