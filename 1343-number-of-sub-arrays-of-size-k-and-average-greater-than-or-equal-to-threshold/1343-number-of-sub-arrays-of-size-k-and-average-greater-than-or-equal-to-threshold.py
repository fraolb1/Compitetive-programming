class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = sum(arr[:k-1])
        l = 0
        count = 0
        for i in range(k-1,len(arr)):
            curr += arr[i]
            if curr/k >= float(threshold):
                count += 1
            curr -= arr[l]
            l += 1
        return count