class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen == 0:
            return s
        start = end = 0
        cur = 0

        while cur < slen:
            lcnt = cur
            lp = rp = cur
            while rp != slen - 1 and s[rp + 1] == s[lp]:
                rp += 1

            rcnt = slen - 1 - rp

            x = min(lcnt, rcnt)
            cnt = x
            for o in range(x + 1):
                if s[lp - o] != s[rp + o]:
                    cnt = o - 1
                    break
            loc1 = lp - cnt
            loc2 = rp + cnt
            if loc2 - loc1 > end - start:
                start, end = loc1, loc2

            cur = rp + 1

        return s[start:end + 1]
