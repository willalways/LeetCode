class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen, plen = len(s), len(p)
        if slen == 0 or plen == 0:
            return self.isMatch(s, p[2:]) if plen >= 2 and p[1] == '*' else slen == plen
        if plen == 1 or p[1] != '*':
            return False if p[0] != '.' and s[0] != p[0] else self.isMatch(s[1:], p[1:])
        return self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) if s[0] == p[0] or p[0] == '.' else self.isMatch(s, p[2:])
