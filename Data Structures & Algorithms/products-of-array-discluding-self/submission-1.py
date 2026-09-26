class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # update left products in-place
        l = 1
        for i in range(1, len(nums)):
            l *= nums[i-1]
            res[i] *= l

        # update right products in-place
        r = 1
        for i in range(len(nums) - 2, -1, -1):
            r *= nums[i+1]
            res[i] *= r
        
        return res