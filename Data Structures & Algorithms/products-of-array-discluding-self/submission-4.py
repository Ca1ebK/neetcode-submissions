class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [0] * len(nums)
        postfix[-1] = 1

        # [1, 2, 3, 4]
        # pre = [1, 1, 2, 6]
        # pos = [2, 12, 4, 1]
        # fill the prefix array
        # multiply the element preceding the current index in nums
        # with the last element of prefix
        for i in range(1, len(nums)):
            prefix.append(nums[i-1] * prefix[-1])
        
        # fill the postfix array
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        
        return res