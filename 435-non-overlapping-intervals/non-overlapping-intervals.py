class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval[1])
        removed = 0
        last_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= last_end:
                last_end = interval[1]
            else:
                removed += 1
        return removed

        