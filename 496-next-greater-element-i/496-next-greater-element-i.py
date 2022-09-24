class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_list = list()
        for i in range(len(nums1)):
            index = -1
            flag = True
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    index = 1
                elif nums2[j] > nums1[i] and index != -1:
                    new_list.append(nums2[j])
                    flag = False
                    break
            if flag:
                new_list.append(-1)
        return new_list