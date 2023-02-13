class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [-1] + [index for index,value in enumerate(nums) if value % 2 == 1] + [len(nums)]
        res = 0

        for j,end in enumerate(odds[k:-1],k):
            ends = odds[j + 1] - end
            starts = odds[j - k + 1] - odds[j-k]
            res += starts * ends
        return res
