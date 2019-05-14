class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        slen = len(s)
        step = numRows * 2 - 2
        group = slen // step
        last = slen % step
        if last != 0:
            group += 1
        ret = ''

        # deal with each line
        for i in range(numRows):
            # deal with each group
            for j in range(group):
                basic = step * j
                if basic + i < slen:
                    ret += s[basic + i]
                x = basic + step - i
                if x < slen and i != 0 and i != numRows - 1:
                    ret += s[x]
        return ret