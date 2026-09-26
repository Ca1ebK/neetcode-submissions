class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1

        res = [1] * len(nums)

        # [1, 2, 3, 4]
        # pre = [1, 1, 2, 6]
        # pos = [24, 12, 4, 1]
        # fill the prefix array
        # multiply the element preceding the current index in nums
        # with the last element of prefix
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            res[i] = prefix
        
        # fill the postfix array
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        
        return res