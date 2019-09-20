from collections import Counter
import copy

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        slen = len(s)
        wllen = len(words)
        if not slen or not wllen:
            return []

        wlen = len(words[0])
        if not wlen:
            return []

        mlen = min(slen - wllen * wlen + 1, wlen)
        wc = Counter(words)
        ret = []
        for i in range(mlen):
            wq = []
            loop = (slen - i) // wlen
            for j in range(loop):
                subword = s[i + j * wlen:i + j * wlen + wlen]
                wq.append(subword)
                
            start = cur = 0
            end = len(wq)
            tmp = copy.copy(wc)
            while cur < end:
                if wq[cur] not in tmp:
                    while start < cur:
                        tmp[wq[start]] += 1
                        start += 1
                    cur += 1
                    start = cur
                    continue
                
                if tmp[wq[cur]] > 0:
                    tmp[wq[cur]] -= 1
                    if cur - start == wllen - 1:
                        ret.append(i + start * wlen)
                        tmp[wq[start]] += 1
                        start += 1

                    cur += 1
                else:
                    tmp[wq[start]] += 1
                    start += 1
                    if cur < start:
                        cur = start
        
        return ret     