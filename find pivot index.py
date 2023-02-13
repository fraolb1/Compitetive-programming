class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right,left = sum(nums),0
        for index,value in enumerate(nums):
            right -= value
            if left == right:
                return index
            left += value
        return -1
