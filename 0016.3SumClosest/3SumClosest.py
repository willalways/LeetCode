class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        numslen = len(nums)
        closest = 0x7fffffff
        for i in range(numslen - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = numslen - 1
            while j < k:
                three = nums[i] + nums[j] + nums[k]
                dis = abs(three - target)
                if dis < abs(closest - target): closest = three
                if three > target:
                    k -= 1
                elif three < target:
                    j += 1
                else:
                    break
            if j < k:
                break
        return closest
                
        