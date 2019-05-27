class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def func(left, right, curstr, glolist):
            if left == 0:
                glolist.append(curstr + ')' * right)
                return
            if left == right:
                func(left - 1, right, curstr + '(', glolist)
            elif left < right:
                func(left - 1, right, curstr + '(', glolist)
                func(left, right - 1, curstr + ')', glolist)
        left, right, curstr, glolist = n, n, '', []
        func(n, n, curstr, glolist)

        return glolist
