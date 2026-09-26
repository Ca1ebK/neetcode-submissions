class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        Proposed solution:
        * for each number in nums, apply the two sum 
        * approach to the remainder of the array
        '''

        triplets = []

        for i in range (0, len(nums) - 2):
            vals = {}
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                comp = target - nums[j]
                res = sorted([nums[i], comp, nums[j]])
                if comp in vals.values() and res not in triplets:
                    triplets.append(res)
                else:
                    vals[j] = nums[j]
        
        return triplets