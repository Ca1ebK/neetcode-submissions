class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        curr_streak = 0
        max_streak = 0
        for n in nums:
            if n - 1 not in seen:   # n is the start of a sequence
                curr_streak = 1
                i = n
                while i + 1 in seen:
                    curr_streak += 1
                    i += 1
                max_streak = max(max_streak, curr_streak)
        return max_streak
