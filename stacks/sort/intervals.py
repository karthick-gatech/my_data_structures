# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


class interval(object):
    def __init__(self, start,end):
        self.start = start
        self.end = end

class Solution(object):

    def __init__(self, intervals):
        self.intervals = intervals

    def merge(self):
        self.intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in self.intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged


def main():
    i = interval(1,2)
    j = interval(3,5)
    k = interval(2,4)
    intervals = list()
    intervals.append(i)
    intervals.append(j)
    intervals.append(k)
    s = Solution(intervals)
    for i in intervals:
        print i.__dict__

    merged = s.merge()
    for i in merged:
        print i.__dict__


main()