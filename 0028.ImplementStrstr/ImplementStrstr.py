class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1, len2 = len(haystack), len(needle)
        if len1 < len2:
            return -1
        if len2 == 0:
            return 0
        for i in range(len1 - len2 + 1):
            if haystack[i:i + len2] == needle:
                return i
        return -1
