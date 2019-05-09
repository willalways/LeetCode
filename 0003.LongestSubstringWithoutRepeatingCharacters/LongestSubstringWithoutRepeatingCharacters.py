class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = {}
        start = 0
        end = 0
        strlen = len(s)
        maxlen = 0

        for end in range(strlen):
            if s[end] in x and x[s[end]] >= start:
                maxlen = max(end - start, maxlen)
                start = x[s[end]] + 1
            x[s[end]] = end
        maxlen = max(strlen - start, maxlen)

        return maxlen
