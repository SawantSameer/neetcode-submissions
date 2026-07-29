class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        output = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0]> output[1]:
                res.append(output)
                output = intervals[i]
            else:
                output = [min(output[0], intervals[i][0]), max(output[1], intervals[i][1])]

        res.append(output)
        return res