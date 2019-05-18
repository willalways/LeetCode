class Solution(object):
    def isMatch(self, text, pattern):
        dic = {}
        tlen,plen = len(text),len(pattern)

        def lookij(i, j):
            if (i, j) in dic: return dic[i, j]
            
            # terminal
            if i == tlen or j == plen:
                if i != tlen:
                    dic[i, j] = False
                elif j == plen:
                    dic[i, j] = True
                elif plen - j == 1 or pattern[j + 1] != '*':
                    dic[i, j] = False
                else: #if plen - j >= 2 and pattern[j + 1] == '*':
                    dic[i, j] = lookij(i, j + 2)
                return dic[i, j]
  
            # pattern[j + 1] != '*' 
            if plen - j == 1 or plen - j >= 2 and pattern[j + 1] != '*':
                if text[i] != pattern[j] and pattern[j] != '.':
                    dic[i,j] = False
                else:
                    dic[i,j] = lookij(i + 1, j + 1)
                return dic[i, j]
            else:
                if text[i] != pattern[j] and pattern[j] != '.':
                    dic[i, j] = lookij(i, j + 2)
                else:
                    dic[i, j] = lookij(i, j + 2) or lookij(i + 1, j)
                return dic[i, j]
                    
        return lookij(0, 0)