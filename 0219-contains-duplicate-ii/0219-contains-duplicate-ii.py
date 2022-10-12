class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = dict()
        flag = True
        for i,n in enumerate(nums):
            if n in temp:
                
                if abs(i - temp[n]) <= k:
                    return True
                else:
                    temp[n] = i
                    continue
            else:
                temp[n] = i
        return False