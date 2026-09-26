class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1, 1, 1, 2, 2, 3]
        # hash map to keep track of the frequencies of each element
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        # {1:3, 2:2, 3:1}
        
        # bucket sort
        # make an array with the indices representing the frequencies
        # the array stores lists of the elements in nums that have those
        # frequencies

        freq = []
        for i in range(len(nums)+2):
            freq.append([])
        
        # [[], [], [], [], [], [], []]

        # fill the freq array

        # for i in range(1, len(freq)):
        #     freq[counts[i]].append(counts[])

        for num, cnt in counts.items():
            freq[cnt].append(num)
        
        # [[], [3], [2], [1], [], [], []]

        # result array
        res = []

        # retrieve the top K elements
        i = len(nums)
        while k > 0:
            if not freq[i]:
                i -= 1
                continue
            else:
                res.append(freq[i].pop())
                k -= 1
        
        return res