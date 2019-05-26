class Solution:
    def isValid(self, s: str) -> bool:
        stack, ch = [], ''
        for ch in list(s):
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                chp = stack.pop()
                if ch == ')' and chp == '(' or ch == ']' and chp == '[' or ch == '}' and chp == '{':
                    continue
                return False
        if len(stack) == 0:
            return True
        return False
