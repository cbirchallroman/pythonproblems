class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        previous = s[0]
        total = 0;

        for char in s:
            if translation[previous] < translation[char]:
                total -= translation[previous]
                total += translation[char] - translation[previous]
            else:
                total += translation[char]
            previous = char
        return total
