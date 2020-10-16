def find_Kth_smallest_number(nums, k):
    # TODO: Write your code here
    charFrequency = {}
    for char in nums:
        if char not in charFrequency:
            charFrequency[char] = 1
        charFrequency[char] += 1
    # x = sorted(charFrequency.items())
    # print(k,": ",x)
    return sorted(charFrequency.items())[k - 1][0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
