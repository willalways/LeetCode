class Solution:
    def romanToInt(self, s: str) -> int:
        romanmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        slen = len(s)
        i,ret = 0,0
        
        while i < slen - 1:
            if romanmap[s[i]] < romanmap[s[i + 1]]:
                ret += romanmap[s[i + 1]] - romanmap[s[i]]
                i += 2
            else:
                ret += romanmap[s[i]]
                i += 1
        if i == slen - 1:
            ret += romanmap[s[-1]]
        return ret