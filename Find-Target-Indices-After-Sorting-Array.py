class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        new_list = list()
        for index, num in enumerate(nums):
            if num == target:
                new_list.append(index)
            else:
                continue
        return new_list
