class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nummap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        tmplist = []
        lendigits = len(digits)
        if not lendigits:
            return []
        pastlist = nummap[digits[-1]]
        for i in range(lendigits - 2, -1, -1):
            for ch1 in nummap[digits[i]]:
                for ch2 in pastlist:
                    ch3 = ch1 + ch2
                    tmplist.append(ch3)
            pastlist = tmplist
            tmplist = []
        return pastlist
