class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        numslen = len(nums)
        nums.sort()
        ret = []
        for i in range(numslen - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] * 4 > target: break
            if nums[-1] * 4 < target: break
            for j in range(i + 1, numslen - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                if nums[j] * 3 > (target - nums[i]): break
                if nums[-1] * 3 < (target - nums[i]): break
                k,l = j + 1,numslen - 1
                while k < l:
                    if nums[k] * 2 > (target - nums[i] - nums[j]): break
                    if nums[-1] * 2 < (target - nums[i] - nums[j]): break
                    fsum = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if fsum == target:
                        ret.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < numslen - 1 and nums[k + 1] == nums[k]: k += 1
                        while l > j + 1 and nums[l - 1] == nums[l]: l -= 1
                        l,k = l - 1,k + 1
                    elif fsum > target:
                        while l > j + 1 and nums[l - 1] == nums[l]: l -= 1
                        l -= 1
                    else:
                        while k < numslen - 1 and nums[k + 1] == nums[k]: k += 1
                        k += 1
                    
                
        return ret