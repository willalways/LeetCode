class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        numlen = len(nums)
        for i in range(numlen):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i