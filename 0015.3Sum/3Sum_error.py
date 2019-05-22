class Solution:
    # O(n * n * logn)   Time Limit Exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numlen = len(nums)
        ret = []
        ij = []
        for i in range(numlen - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, numlen - 1):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                k = 0 - nums[i] - nums[j]
                if k < nums[j]: break
                if self.binsearch(nums[j + 1:], k) == True:
                    tmp = [nums[i], nums[j], k]
                    if tmp not in ret:
                        ret.append(tmp)
        return ret
    
    def binsearch(self, nums: List[int], target):
        numslen = len(nums)
        left = 0
        right = numslen - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False