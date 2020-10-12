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
