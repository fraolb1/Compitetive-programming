class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = list()
        for i in s:
            if len(s) >= 2:
                if i == "[" or i == "(" or i == "{":
                    stack1.append(i)
                elif i == "]" and len(stack1) != 0 and stack1[-1] == "[":
                    stack1.pop()
                elif i == "}" and len(stack1) != 0 and stack1[-1] == "{":
                    stack1.pop()
                elif i == ")" and len(stack1) != 0 and stack1[-1] == "(" :
                    stack1.pop()
                else:
                    return False
            else:
                return False
        return len(stack1) == 0
