def mergeIntervals(newInterval):
    if not len(newInterval):
        return newInterval
    newIntervalX = [newInterval[0]]
    previous = newIntervalX[0]
    for i in range(1, len(newInterval)):
        current = newInterval[i]
        if current[0] <= previous[1]:
            previous[1] = current[1] if current[1] >= previous[1] else previous[1]
        else:
            newIntervalX.append(current)
            previous = current
    return newIntervalX
#########################################################################
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Input: intervals = [[1, 4], [0, 4]]
Output: [[1,4]]
"""

#########################################################################
Intervals = [[0, 4], [14, 18], [18, 22], [33, 37], [36, 40], [39, 43]]
print("actual Intevals", Intervals)
print(mergeIntervals(Intervals))

ix2 = [[1, 4], [0, 4]]
ix2.sort()
print("actual Intevals", ix2)
print(ix2)

print(mergeIntervals(ix2))
ix3 = [[1, 4], [2, 3]]
ix3.sort()
print("actual Intevals", ix3)
print(mergeIntervals(ix3))
