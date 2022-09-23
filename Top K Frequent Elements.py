from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = dict(Counter(nums))
        new_dict = sorted(new_dict.items(),key = lambda item: item[1],  reverse = True)
        new_list = list()
        while k != 0:
            k -= 1
            new_list.append(new_dict[k][0])
        return new_list
