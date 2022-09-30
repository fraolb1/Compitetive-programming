class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        count = nums.count(0)
        while index < len(nums)-count:
            if nums[index] == 0:
                temp = nums.pop(index)
                nums.append(temp)
            else:
                index += 1