class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(key=lambda a:a[0])
        for index,value in enumerate(cars):
            cars[index] = (target-value[0])/value[1]
        res = 0
        stack = []
        flag = None
        for i in range(len(cars)-1,-1,-1):
            flag = False
            while stack and stack[-1] < cars[i]:
                flag = True
                stack.pop()
            if len(stack) == 0 and flag:
                res += 1
            stack.append(cars[i])
        if stack:
            res += 1
        return res
