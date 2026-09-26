class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        
        n = len(nums)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return