class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strslen = len(strs)
        if not strslen:
            return ''
        if strslen == 1:
            return strs[0]

        cnt = 0
        while True:
            xx = False
            for st in strs:
                try:
                    if st[cnt] != strs[0][cnt]:
                        xx = True
                        break
                except:
                    xx = True
            if xx == True:
                if cnt == 0:
                    cnt = -1
                break
            cnt += 1

        if cnt >= 0:
            return strs[0][:cnt]
        return ""
