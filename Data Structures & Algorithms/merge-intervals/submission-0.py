class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Sort the 2D list intervals
        Add the first interval to res
        Loop through the rest of the intervals:
          - if the start of the current interval is less than the
          - end of the interval in res, then merge the lists,
          - meaning set the end of the list in res to the max
          - of the current interval's end and the one in res's end
          - else just append the current interval to res
        Return res

        Time: O(n log n) (timsort)
        Space: O(n*m)
        '''

        if len(intervals) == 1:
            return intervals

        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        
        return res