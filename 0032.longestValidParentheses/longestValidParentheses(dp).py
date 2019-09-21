import string

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        slen = len(s)
        dp = [0 for i in range(slen)]
        mx = 0
        for i in range(1, slen):
            if s[i] == '(':
                dp[i] = 0
            elif s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
            else:
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    # print("dp[%d] = %d" % (i, dp[i]))
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
                        
            mx = max(mx, dp[i])
        return mx
                