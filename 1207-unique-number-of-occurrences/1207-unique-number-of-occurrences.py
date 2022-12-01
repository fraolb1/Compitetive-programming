class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new_dic = dict(Counter(arr))
        curr = -1
        new_dic = {k: v for k, v in sorted(new_dic.items(), key=lambda item: item[1])}
        for key , value in new_dic.items():
            if curr == value:
                return False
            curr = value
        return True