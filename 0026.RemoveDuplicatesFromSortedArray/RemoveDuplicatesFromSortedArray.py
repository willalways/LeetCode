'''
# use del
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numslen,i,ret = len(nums),1,1
        if numslen <= 1: return numslen
        while i < numslen:
            if nums[i] != nums[i - 1]:
                ret,i = ret + 1, i + 1
            else:
                del nums[i]
                numslen -= 1
        return ret
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numslen, i, ret = len(nums), 1, 1
        if numslen <= 1:
            return numslen
        for i in range(1, numslen):
            if nums[i] != nums[i - 1]:
                nums[ret] = nums[i]
                ret += 1
        return ret
