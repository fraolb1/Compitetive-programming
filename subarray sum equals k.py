class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sums = defaultdict(int)
        running_sum = 0
        for num in nums:
            running_sum += num
            if running_sum == k:
                res += 1
            if running_sum - k in sums:
                res += sums[running_sum -k]
            sums[running_sum] += 1
        return res
