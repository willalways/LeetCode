class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0: return 0
        strlist = list(str.split(' ')[0])
        for i in range(1,len(strlist)):
            if strlist[i] < '0' or strlist[i] > '9':
                strlist[i] = ' '
                break
        str = ''.join(strlist).split(' ')[0]
        try:
            ret = int(str)
        except:
            return 0

        if ret > 2147483647: return 2147483647
        elif ret < -2147483648: return -2147483648
        else: return ret
        