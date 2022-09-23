class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new_list = list()
        for i in nums:
            new_list.append(int(i))
        new_list.sort()
        return(str(new_list[len(nums) - k]))
