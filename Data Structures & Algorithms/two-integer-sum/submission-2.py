class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal (Hash Map)
        # Time: O(n)
        # Space: O(n)

        seen = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp not in seen:
                seen[n] = i
            else:
                return [seen[comp], i]
        
        return