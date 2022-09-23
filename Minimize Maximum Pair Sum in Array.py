class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_num = 0
        while right > left and len(nums) >= 2:
            if nums[right] + nums[left] >= max_num:
                max_num = nums[right] + nums[left]
                right -= 1
                left += 1
            else:
                right -= 1
                left += 1
        return max_num
