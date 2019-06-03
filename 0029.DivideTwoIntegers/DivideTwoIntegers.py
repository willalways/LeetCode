class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s1 = 1 if dividend > 0 else -1
        s2 = 1 if divisor > 0 else -1

        if dividend == -2**31:
            if divisor == -1:
               return 2**31 - 1
            else:
                return s1 * s2 * (self.divide(abs(abs(divisor) - abs(dividend)), abs(divisor)) + 1)

        divisor = abs(divisor)
        dividend = abs(dividend)
        if divisor > dividend: return 0
        tmp = divisor
        ret = 0

        for i in range(31):
            tmp = divisor << i
            ret = i
            if tmp > dividend:
                break

        return s1 * s2 * (2 ** (ret - 1) + self.divide(dividend - (tmp >> 1), divisor))
        