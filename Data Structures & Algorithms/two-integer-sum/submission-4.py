class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Sorted Solution
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        n = len(nums)
        indices = []

        for i in range(n):
            indices.append(i)

        new_nums = list(zip(nums, indices))
        sorted_nums = sorted(new_nums, key=lambda num: num[0])

        l = 0
        r = n - 1

        while l < r:
            total = sorted_nums[l][0] + sorted_nums[r][0]
            if total == target:
                return sorted([sorted_nums[l][1], sorted_nums[r][1]])
            elif total < target:
                l += 1
            else:
                r -= 1
        
        return