"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        lst = sorted(intervals, key=lambda x: x.start)
        #starts = [elem.start for elem in intervals]
        prev = lst[0].end
        for curr in lst[1:]:
            if curr.end < prev:
                return False
            prev = curr.end
        return True