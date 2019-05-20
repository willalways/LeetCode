class Solution:
    def maxArea(self, height: List[int]) -> int:
        llen = len(height)
        ret = 0
        i,j = 0,llen - 1
        while (i < j):
            if height[i] <= height[j]:
                ret = max(ret, (j - i) * height[i])
                i += 1
            else:
                ret = max(ret, (j - i) * height[j])
                j -= 1
        return ret