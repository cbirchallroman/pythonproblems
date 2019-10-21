class Solution:
    def reverse(self, x: int) -> int:
        reverse = str(abs(x))[::-1]
        
        if (int("-" + reverse) < -2 ** 31 or int(reverse) > 2 ** 31 - 1):
            return 0
        return (int("-" + reverse) if x < 0 else int(reverse))