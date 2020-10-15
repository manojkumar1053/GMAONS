from collections import defaultdict


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        memo = defaultdict(int)
        for character in S:
            memo[character] += 1

        char_max = max(memo.items(), key=lambda x: x[1])
        memo.pop(char_max[0])
        if char_max[1] - 1 > sum(memo.values()):
            return ""

        ret_list = [char_max[0]] * char_max[1]
        i = 0
        for key in memo:
            for _ in range(memo[key]):
                ret_list[i % char_max[1]] += key
                i += 1
        return "".join(ret_list)
