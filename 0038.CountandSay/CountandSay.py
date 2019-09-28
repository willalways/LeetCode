class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        past = '1'
        for i in range(2, n+1):
            start = end = 0
            
            # deal with one string.
            out = ''
            for end in range(1, len(past)):
                if past[start] != past[end]:
                    out += str(end - start) + past[start]
                    start = end

            if past[end] == past[end - 1]:
                out += str(end - start + 1) + past[end]
            else:
                out += '1' + past[end]

            past = out
        return past