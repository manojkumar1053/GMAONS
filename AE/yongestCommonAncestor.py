class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYongestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(depthOne, depthTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(depthTwo, depthOne, depthTwo - depthOne)


def getDescendantDepth(descendant, ancestor):
    depth = 0
    while descendant != ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestralTree(lowerDesendant, higherDescendant, diff):
    while diff > 0:
        lowerDesendant = lowerDesendant.ancestor
        diff -= 1
    while lowerDesendant != higherDescendant:
        lowerDesendant = lowerDesendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDesendant
