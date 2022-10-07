class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        res = list()
        flag = False
        if nums.count(0) > 1:
            return [0] * len(nums)
        for i in nums:
            if i != 0:
                pro *= i
                flag = True
        if not flag:
            pro = 0
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(pro)
                else:
                    res.append(0)
        else:
            res = [pro//i for i in nums]
        return res
            