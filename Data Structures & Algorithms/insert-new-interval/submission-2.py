class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # if newInterval[1] < intervals[0][0]:
        #     intervals.insert(0, newInterval)
        #     return intervals
        
        # if newInterval[0]>intervals[-1][1]:
        #     intervals.append(newInterval)
        #     return intervals
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res