class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in seen:
                seen[nums[i]] = i
            else:
                return [min(i, seen[comp]), max(i, seen[comp])]
        return