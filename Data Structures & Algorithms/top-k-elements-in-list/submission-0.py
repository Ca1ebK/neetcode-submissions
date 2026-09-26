from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        nums_sorted = sorted(nums, key=counts.get)
        print(nums_sorted)

        res = [nums_sorted[-1]]

        while len(res) < k:
            n = nums_sorted.pop()
            if n not in res:
                res.append(n)
        
        return res