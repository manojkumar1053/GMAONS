# str1 = "ab"
# str2 = "bc"
# lcs = [[[None, 0, None, None] for row in range(len(str1) + 0)] for column in range(len(str2) + 0)]
# print(lcs)
# print("column: ", len(lcs))
# print("row: ", len(lcs[0]))
#
# print([[[] for i in range(1, 6)] for j in range(1, 3)])
# print([[[i] for i in range(1, 6)] for j in range(1, 3)])
#
# print("************************************************************")
# print([[[i, i ** 2] for i in range(1, 6)] for j in range(1, 3)])
# print([[[i, i ** 2] for i in range(1, 6)] for j in range(1, 3)][1])
# print([[[i, i ** 2] for i in range(1, 6)] for j in range(1, 3)][0][0])
# print([[[i, i ** 2] for i in range(1, 6)] for j in range(1, 3)][0][0][0])
#
# print(None is not None)
#
def getPermutations(array):
    # Write your code here.
    permutataions = []
    permutationHelper(array, [], permutataions)
    return permutataions


def permutationHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)

print(getPermutations([1,2]))
str = "manoj"
ls = []
[ls.append(i) for i in str]
print(ls)

print(getPermutations(ls))
