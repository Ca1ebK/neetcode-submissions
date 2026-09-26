class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums) - 2):
            # skipping duplicate first pointers
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # skip duplicate values for left pointer
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
            
        return res