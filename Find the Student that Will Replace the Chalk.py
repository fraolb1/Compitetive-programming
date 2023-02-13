class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = [chalk[0]]
        for i in range(1,len(chalk)):
             prefix_sum.append(prefix_sum[i-1]+chalk[i])
        left_chalk = k % prefix_sum[len(prefix_sum)-1]
        s , e = 0 , len(prefix_sum)-1 

        while(s<=e):
            mid = s+(e-s)//2
            if prefix_sum[mid] == left_chalk:
                return mid+1
            if prefix_sum[mid-1] <= left_chalk and left_chalk < prefix_sum[mid]:
                return mid
            elif prefix_sum[mid-1] < left_chalk and left_chalk > prefix_sum[mid]:
                s = mid+1
            else:
                e=mid-1

        return mid  
