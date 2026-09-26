class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        rob1 = 0    # two houses ago
        rob2 = 0    # one house ago

        for house in nums:
            current_max = max(rob1 + house, rob2)
            rob1 = rob2
            rob2 = current_max
        
        return rob2