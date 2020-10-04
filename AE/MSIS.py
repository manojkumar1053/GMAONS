def maxSumIncreasingSubsequence(array):
    # Write your code here.
    if len(array) == 0:
        return []
    seq = [None for x in range(len(array))]
    maxSumIdx = 0
    sums = array[:]
    for i in range(len(array)):
        currentNum = array[i]
        for j in array(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                seq[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSumarray(array, seq, maxSumIdx)]


def buildSumarray(array, seq, currentIdx):
    seqx = []
    while currentIdx is not None:
        seqx.append(array[currentIdx])
        currentIdx = seq[currentIdx]
    return list(reversed(seqx))
