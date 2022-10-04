class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        new_list = list()
        for i in gain:
            h += i
            new_list.append(h)
        new_list.append(0)
        return sorted(new_list)[-1]