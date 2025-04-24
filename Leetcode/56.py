# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        result = []
        p1 = 0
        p2 = 0
        num_intervals = len(intervals)
        while p1<num_intervals:
            start_index = intervals[p1].start
            end_index = intervals[p1].end
            while p2<num_intervals and intervals[p2].start<=end_index:
                end_index = max(intervals[p2].end, end_index)
                p2+=1
            result.append(Interval(start_index, end_index))
            p1 = p2
        return result


if __name__ == "__main__":
    s = Solution()
    t1 = [Interval(x[0], x[1]) for x in [[1,3],[2,6],[15,18],[8,10]]]
    for interval in s.merge(t1):
        print(interval.start, interval.end)
    t2 = [Interval(x[0],x[1]) for x in [[1,4],[4,5]]]
    for interval in s.merge(t2):
        print(interval.start, interval.end)