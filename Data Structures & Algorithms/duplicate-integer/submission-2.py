class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Two Pointers Approach
        # Time Complexity: O(n*log(n))
        # Space Complexity: O(1)
        
        nums.sort()

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            else:
                i, j = i + 1, j + 1
        
        return False