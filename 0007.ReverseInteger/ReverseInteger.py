class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -1 * x
        y = int(str(x)[::-1])
        return 0 if y > 2 ** 31 else sign * y
