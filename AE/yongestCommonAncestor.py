def getYongestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)


def getDescendantDepth(descendant, ancestor):
    depth = 0
