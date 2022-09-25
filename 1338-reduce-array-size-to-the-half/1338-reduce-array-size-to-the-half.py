from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        new_dict = dict(Counter(arr))
        count = 0
        target = len(arr)//2
        for value in sorted(new_dict.values(), reverse = True ):
            if target <= 0:
                return count
            target -= value
            count += 1
        return count