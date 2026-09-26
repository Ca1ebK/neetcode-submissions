class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Most optimal solution (?)
        # Time: O(n)
        # Space: O(n)
        nums_set = set()

        for n in nums:
            if n in nums_set:
                return True
            nums_set.add(n)
        
        return False