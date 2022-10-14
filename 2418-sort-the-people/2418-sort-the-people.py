class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = dict()
        res = list()
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        dic = sorted(dic.items(), key = lambda item: item[0], reverse = True)
        for i in dic:
            res.append(i[1])
        return res