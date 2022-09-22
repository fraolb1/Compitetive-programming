class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]):
        new = list()
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    temp += 1
                else:
                    continue
            new.append(temp)
        return new
