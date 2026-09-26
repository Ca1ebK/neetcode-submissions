from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        res = []

        # for i in range(k):
        #     res.append(buckets[-1][-1])
        #     buckets[-1].pop()

        while len(res) < k:
            if len(buckets[-1]) > 0:
                res.append(buckets[-1].pop())
            else:
                buckets.pop()
        
        return res