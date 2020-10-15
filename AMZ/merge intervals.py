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
