class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        # find where [startTime, endTime] would be inserted
        idx = bisect.bisect_left(self.intervals, [startTime, endTime])
        # overlapping
        if(idx > 0 and self.intervals[idx - 1][1] > startTime):
            return False

        # check right interval
        if(idx < len(self.intervals) and endTime > self.intervals[idx][0]):
            return False

        self.intervals.insert(idx, [startTime, endTime])
        return True